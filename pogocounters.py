import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

gc = gspread.authorize(credentials)
wks = gc.open("PoGo Raid Counters").sheet1
print("Spreadsheet opened\n", flush=True)

col1 = wks.col_values(1)
col2 = wks.col_values(2)
col3 = wks.col_values(3)
print("Columns opened\n", flush=True)

all_records = wks.get_all_records()
print("All records have been fetched\n", flush=True)

keys = []
for key in all_records[1]:
    keys.append(key)
print(" | ".join(keys))
#print(all_records[1].keys()) # not what I want
for column in all_records:
    print(column["Raid boss"], "|", column["Type"], "|", column["Weaknesses"])

"""i = 0
for value in col1:
    if not value:
        break
    #print(wks.cell(i, 1).value + "   " + wks.cell(i, 2).value + "   " + wks.cell(i, 3).value, flush=True)
    #print(wks.cell(i, 1).value, flush=True) #seems a bit faster to print cells directly
    # These are both slow because it makes 1+ API calls per iteration. 
    print(col1[i] + " " + col2[i] + " " + col3[i], flush=True) # this is much faster, because it just accesses values stored in a list
    i = i + 1"""

print(wks.row_count)
print(wks.col_count)
print(wks.findall("Water"))
