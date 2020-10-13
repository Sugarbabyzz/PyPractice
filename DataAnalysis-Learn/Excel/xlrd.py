import xlrd  # Read EXCEL

data = xlrd.open_workbook('example.xlsx')  # Get an excel

table = data.sheet_by_index(0)  # Get a Sheet / sheet_by_name can be used, too


for i in range(table.nrows):  # Get the number of row or col
    print(table.row_values(i))  # Get the value of row or col

print('####################')

print("(0,0) cell's value is ", table.cell(0, 0).value)  # Get the value of a specific cell

import xlwt  # Write an EMPTY EXCEL

workbook = xlwt.Workbook(encoding='ascii')  # Get an excel

worksheet = workbook.add_sheet('My WorkSheet')  # Create a sheet

worksheet.write(0, 0, label='Row 0, Column 0 Value')  # Write a cell

workbook.save('Excel_Workbook.xls')


from xlrd import open_workbook
from xlutils.copy import copy

rb = open_workbook('example.xlsx')  # Get an EXCEL

# write() method can't be used by sheet_by_index() but get_sheet() can

rs = rb.sheet_by_index(0)

wb = copy(rb)

ws = wb.get_sheet(0)
ws.write(0, 0, 'changed!')

wb.save('saved_excel.xlsx')








