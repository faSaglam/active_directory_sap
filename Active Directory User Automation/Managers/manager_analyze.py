import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 700)


#Take data from managers xlsx
df = pd.read_excel('Managers/managers.xlsx')
df["SF - Manager Fullname"].isnull().values.any()
df["SF - Manager Fullname"].info()



#Get-ADUser -Identity arnoldkuuku.griffin |Set-ADUser -EmployeeID


#turkish characters transfer to english characters
turkish_to_english = str.maketrans(
    "åáçğıöşüÇĞİÖŞÜ",
    "aacgiosuCGIOSU"
)

def convert_turkish_to_english(text):
    return text.translate(turkish_to_english)

# Some user have 3 names.
# Ex: Omer Faruk Saglam. It transforms omer.faruk.saglam but it does not match with AD rules
# For handle that, transform_names function delete first "."
def transform_names (name):
    parts = name.split(".")
    if len(parts) == 3:
        return parts[0]+parts[1]+"."+parts[2]
    else:
        return parts[0]+"."+parts[1]


# Women get married and changes their names. Exception function handles that. You should enter their name
#  {from excel : what it is in AD}

def exception(account_name):
    exceptions = {
        "ahmetmehmet.osman": "ahmet.osman",
        "derya.deniz": "d.deniz",
    }
    return exceptions.get(account_name, account_name)

# TRANSFORM SAP Names to AD Account Name
# delete empty rows
df = df.dropna(subset=["SF - Manager Fullname"])

# make it ad account name
df["SF - Manager Fullname"] = df["SF - Manager Fullname"].str.lower().replace(" ", ".", regex=True)
df["SF - Manager Fullname"] = df["SF - Manager Fullname"].apply(convert_turkish_to_english)
df["SF - Manager Fullname"] = df["SF - Manager Fullname"].apply(transform_names)
df["SF - Manager Fullname"] = df["SF - Manager Fullname"].apply(exception)

# Transform to powershell command
powershell_command_lines = []
for index, row in df.iterrows():
    employee_name = row["AD - SamAccountName"]
    manager_name = row["SF - Manager Fullname"]
    output = f"Get-ADUser -Identity {employee_name} |Set-ADUser -Manager {manager_name}"
    powershell_command_lines.append(output)


print(powershell_command_lines)

file_path="Managers/manager_update.txt"
with open(file_path, 'w', encoding='utf-8') as file:
    for line in powershell_command_lines:
        file.write(line + '\n')
        print(line)



