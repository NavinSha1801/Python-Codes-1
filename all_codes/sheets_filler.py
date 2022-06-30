import pygsheets

sheet = pygsheets.authorize(client_secret='client_secret.json')

sheet_open = sheet.open('samplesheet')
print(sheet_open)