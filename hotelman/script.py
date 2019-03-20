import xlrd
worksheet = xlrd.open_workbook("HII.xlsx").sheet_by_name("Sheet1")

for row in range(63):
    for col in range(1,3,2):
        room_no = worksheet.cell_value(row,col)
        details = worksheet.cell_value(row,col+1)
        Room.objects.create(room_no=str(room_no).strip(".0"),description=details)
        print(details)
