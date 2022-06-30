import gspread

#credentials
acc = gspread.service_account('D:\\git_files\\Python-Codes-1\\all_codes\\new_id.json')

#Openning All FIles
first_sheet = acc.open('candidates')
second_sheets = acc.open('rough')   
all_data_merge = acc.open('samplesheet')

#accessing sheets
fs_s1 = first_sheet.worksheet('Sheet1')
ss_s1 = second_sheets.worksheet('Sheet1')
adm_s1 = all_data_merge.worksheet('Sheet1')

#fetching name colum from candiates file
name_data_fs_s1 = fs_s1.col_values(2)

#printing data in nicer format:
temp = 0
for i in name_data_fs_s1:
    print(f'{temp} -> {i}')
    temp+=1

#entering data form user 
no = input('Enter number of person: ')
while True:
    if no.isdigit():
        no = int(no)
        break
    else:
        no = input("Enter number only: ")

actual_name = name_data_fs_s1[no]

#finding data from candidates to rough
data = ss_s1.find(actual_name)

#converting gspread cell to string
data = str(data)

#extracting Row value 
lst = data.split(' ')
row_coloms = lst[1]
row_value = 0

for i in row_coloms:
    if i.isdigit():
        i = int(i)
        row_value = (row_value*10)+i
    elif i =='C':
        break

#fetching row value
row_data = ss_s1.row_values(row_value)
adm_s1.append_row(row_data)





