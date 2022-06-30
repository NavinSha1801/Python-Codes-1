import gspread

service_account = gspread.service_account(filename='newservice.json')
sheet1 = service_account.open('samplesheet')
worksheets1 = sheet1.worksheet('Sheet1')
worksheets2 = sheet1.worksheet('Sheet2')

sheet2 = service_account.open('rough')
worksheet1 = sheet2.worksheet('Sheet1')
worksheet1.update(worksheets1.get_all_values)




