import gspread
from oauth2client.service_account import ServiceAccountCredentials

SCOPE = ['https://spreadsheets.google.com/feeds']

CREDENTIALS = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', SCOPE)

GC = gspread.authorize(CREDENTIALS)
WKS = GC.open("PoGo Raid Counters").sheet1
print("Spreadsheet opened\n", flush=True)

"""col1 = wks.col_values(1)
col2 = wks.col_values(2)
col3 = wks.col_values(3)
print("Columns opened\n", flush=True)"""

ALL_RECORDS = WKS.get_all_records()
print("All records have been fetched\n", flush=True)

def print_headers():
    keys = []
    for key in ALL_RECORDS[0]:
        keys.append(key)
    print(" | ".join(keys))
    #print(all_records[1].keys()) # not what I want


def print_all_bosses():
    print_headers()
    for column in ALL_RECORDS:
        print(column["Raid boss"], "|", column["Type"], "|", column["Weaknesses"])

#print_all_bosses()

"""i = 0
for value in col1:
    if not value:
        break
    #print(wks.cell(i, 1).value + "   " + wks.cell(i, 2).value + "   " + wks.cell(i, 3).value, flush=True)
    #print(wks.cell(i, 1).value, flush=True) #seems a bit faster to print cells directly
    # These are both slow because it makes 1+ API calls per iteration. 
    print(col1[i] + " " + col2[i] + " " + col3[i], flush=True) # this is much faster, because it just accesses values stored in a list
    i = i + 1"""

"""print(wks.row_count)
print(wks.col_count)
print(wks.findall("Water"))"""

def get_raid_boss(name):
    found = False
    headers_printed = False
    print("")
    if name.lower() == "all":
        print_all_bosses()
        return
    for column in ALL_RECORDS:
        if column["Raid boss"].lower() == name.lower():
            if not headers_printed:
                print_headers()
                headers_printed = True
            print(column["Raid boss"], "|", column["Type"], "|", column["Weaknesses"])
            found = True
    if not found:
        print("Could not find boss with name " + "'" + name + "'.")
    print("")

while True:
    get_raid_boss(input("What raidboss do you want info about? "))
    more = input("Do you want info about another boss? (y/n) ")
    print("")
    if more == 'n':
        break
