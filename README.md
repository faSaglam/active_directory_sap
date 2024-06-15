# active_directory_sap
Solve SAP and Active Directory confilicts for IT Team members

## Accounts 
Some times SAP and Active Directory can not match users. For repeatedly unmatched profiles you can use that project for filtering.
You can use it Active Directory Active - SAP Pasive Users.

### 1 Create an excel file.

|AD - EmployeeId |	AD - Fullname |	AD - SamAccountName |	AD - EMail|
| ------------- | ------------- | ------------- | ------------- |
|100001	|Ahmet TURK|ahmet.turk||	
|100002	|Cemre CEMRE|	cemre.cemre	|cemre.cemre@hostname.com|
|100003	|Osman Mehmet Uraz|	osmanmehmet.uraz|	|
### 2 Run project 
It filters the repeatedly false-positive profiles.

## Managers
You can transform to Powershell code SAP Managers information. Copy manager_update texts and paste on powershell on your machine after connect server. 
Easily you can update bulkly profiles.

### 1 Create an excel file.
|AD - EmployeeId|	AD - Fullname	|AD - SamAccountName|	SAP - Manager Fullname|
| ------------- | ------------- | ------------- | ------------- |
|100044	|Derya Deniz	|d.deniz	|Osman Kurtuluş KAHYA|
|100045	|Fındık FISTIK|findik.fistik	|Tahin PEKMEK|
|100046	|Kemal KAMIL	|kemal.kamil	|Celal CEMIL|

### 2 Run project
It creates manager_updates.txt. Copy the codes in txt file and paste powershell 

