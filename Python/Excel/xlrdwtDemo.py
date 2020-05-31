import xlrd,xlwt

workbook = xlrd.open_workbook("testxls.xls")

sheet = workbook.sheet_by_name("Sheet1")

title_row = sheet.row(0)

# print(title_row[0].value)

# print(sheet.nrows)
datas = []

for i in range(1,sheet.nrows):
    data_row = sheet.row(i)
    data ={}
    for j in range(sheet.ncols):
        cell = data_row[j]
       
        if cell.ctype == xlrd.XL_CELL_DATE:
            value = xlrd.xldate_as_datetime(cell.value,0).strftime(("%Y-%m-%d"))
        elif cell.ctype == xlrd.XL_CELL_NUMBER:
            value = int(cell.value)
        else:
            value = cell.value
        
        # print(value)
        data[title_row[j].value] = value
        
    datas.append(data)
print(datas)

workbook = xlwt.Workbook()
sheet = workbook.add_sheet("kins")

for i in range(len(title_row)):
    sheet.write(0,i,title_row[i].value)
    
for i in range(len(datas)):
    data = datas[i]
    value_datas = list(data.values())
    for j in range((len(value_datas))):
        sheet.write(i+1,j,value_datas[j])
        
workbook.save("test2.xlsx")
    
