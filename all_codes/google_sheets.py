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

#storing data into variables
#data is of list type

#first data
fs_s1_data_c = fs_s1.col_values(3)
fs_s1_data_d = fs_s1.col_values(4)
#second data
ss_s1_data_b = ss_s1.col_values(2)
ss_s1_data_c = ss_s1.col_values(3)
ss_s1_data_d = ss_s1.col_values(4)  

#importing data to another sheet

#setting counter
j = 0
while j<len(fs_s1_data_c):
    #adding seond file data into main file
    adm_s1.update_acell(f'A{j+1}',ss_s1_data_b[j])
    adm_s1.update_acell(f'B{j+1}',ss_s1_data_c[j])
    adm_s1.update_acell(f'C{j+1}',ss_s1_data_d[j])
    #adding first file data into main file
    adm_s1.update_acell(f'D{j+1}',fs_s1_data_c[j])
    adm_s1.update_acell(f'E{j+1}',fs_s1_data_d[j])
    #incrimenting counter
    j+=1



#ending
