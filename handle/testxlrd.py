import xlrd

FILE = 'zy_dir.xlsx'

data  = xlrd.open_workbook(FILE)

table = data.sheets()[0]
rows = []

for i in xrange(table.nrows):
    row = table.row_values(i)
    for j in xrange(len(row)):
        row[j] = row[j].encode('utf-8')
    
    #print row

    rows.append(row)
print rows[:20]
    #print row[0], row[1]
    #if i>20:
    #    break
