import pygsheets

sheet = pygsheets.authorize(client_secret='D:\\git_files\\Python-Codes-1\\all_codes\\new_id.json')

sheet_open = sheet.sheet.get('samplesheet')
print(sheet_open)