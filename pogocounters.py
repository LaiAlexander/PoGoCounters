import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name(os.environ.get('CREDS'), scope)

gc = gspread.authorize(credentials)
wks = gc.open("PoGo Raid Counters").sheet1

col1 = wks.col_values(1)
col2 = wks.col_values(2)

print("Spreadsheet opened\n")
i = 1
for value in col1:
    if value:
            print(wks.cell(i, 1).value + "   " + wks.cell(i, 2).value)
    i = i + 1
