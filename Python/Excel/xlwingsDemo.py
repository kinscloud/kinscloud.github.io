#导入xlwings模块
import xlwings as excel

def readExcel(filename,sheetname):
    excelApp = excel.App(False,False)
    excelFile = excelApp.books.open(filename)
    sheet = excelFile.sheets[sheetname]
    rowCount = sheet.used_range.last_cell.row
    colCount = sheet.used_range.last_cell.column
    for line in range(1,rowCount+1):yield sheet.range(line,1).expand('right').value
    excelFile.close()
    excelApp.quit()
    excelApp.kill()

for line in readExcel(r"testxls.xlsx",0):
    print(line)