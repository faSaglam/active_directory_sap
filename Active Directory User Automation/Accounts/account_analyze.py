import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 700)


df = pd.read_excel('Accounts/accounts.xlsx')
print(df.head(100))

emp_id = [1000001,  # Employee 1
          1000002  # Employee 2
          ]
false_positive_to_drop= df[~df['AD - EmployeeId'].isin(emp_id)]

filtered_exl = false_positive_to_drop.to_excel('filtered_accounts.xlsx',index=False)

print(filtered_exl.values)



