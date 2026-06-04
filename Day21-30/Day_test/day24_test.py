from pathlib import Path
import xlrd

path_file = Path(__file__).parent / '装修费用记录.xlsx'
wb = xlrd.open_workbook(path_file)

sheetnames = wb.sheet_names()
print(sheetnames)