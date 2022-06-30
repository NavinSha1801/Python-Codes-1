import gspread

service_acc = gspread.service_account('D:\\git_files\\Python-Codes-1\\all_codes\\new_id.json')
#first File access
sheet1 = service_acc.open('samplesheet')
#pirtuicular sheet access
worksheets1 = sheet1.worksheet('Sheet1')
worksheets2 = sheet1.worksheet('Sheet2')
#second file access
sheet2 = service_acc.open('rough')
worksheet1 = sheet2.worksheet('Sheet1')
#copy one data to another data
# worksheet1.update(worksheets1.get_all_values())
# print(worksheet1.get_all_records())

# for i in worksheet1.col_values(2):
#     print(i)

# for j,k in worksheet1.col_values(1) or worksheet1.col_values(2):
#     print(j)

# i = 1
# for j in worksheet1.col_values(1):
#     print(j,end=' ')
#     for k in worksheet1.col_values(2):
#         print(k)

# dic = dict()
# count = 1
# for j in worksheet1.col_values(2):
#     dic[worksheet1.acell(f'A{count}').value] = j
#     count += 1

# print(dic)

# row_6 = worksheet1.col_values(6)
# print(row_6)
# j = 0
# while j<13:
#     print(row_6[j])
#     j+=1

# j = 0
# while j<13:
#     worksheets1.update_acell(f'F{j+1}',row_6[j])
#     j+=1
