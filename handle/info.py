#coding=utf-8
"""
    从excel获取数据，返回list
"""
import xlrd
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )


#从获取专业数据
def getRows(FILE_READ):
    """
        return 专业数据
    """

    rows = []

    data  = xlrd.open_workbook(FILE_READ)

    table = data.sheets()[0]

    for row in xrange(table.nrows):

        value = table.row_values(row)

        if value[0] == '':
            continue

        rows.append(value)

    #print len(rows)
    rows = rows[1:]
    #handle(rows)

    return rows

#获取zy_xw表中的数据
#学科门类    专业类 专业代码    专业名称    学科代码    一级学科
def getZyXwInfo(FILE_Zy_Xw):
    data  = xlrd.open_workbook(FILE_Zy_Xw)

    table = data.sheets()[0]
    rows = []

    for i in xrange(table.nrows):
        row = table.row_values(i)
        #for j in xrange(len(row)):
            #row[j] = row[j].encode('utf-8')
        
        if row[0]:
            xkml = row[0]
        else:
            row[0] = xkml

        if row[1]:
            zyl = row[1]
        else:
            row[1] = zyl

        rows.append(row)
    rows = rows[1:]

    return rows

#获取专业和院校的数据
def getZyYxInfo(FILE_Zy_Yx):
    rows = []

    data  = xlrd.open_workbook(FILE_Zy_Yx)

    table = data.sheets()[0]

    for row in xrange(table.nrows):

        value = table.row_values(row)
        
        for i, item in enumerate(value):
            try:
                value[i] = item.encode('utf-8')
            except:
                value[i] = item
        
        rows.append(value)

    return rows

#获取xk_info的数据
#学科代码    学科层次    学科名称    学校  附加信息    一级学科
def getXkInfo(FILE_XK):         
    rows = []

    data  = xlrd.open_workbook(FILE_XK)

    table = data.sheets()[0]

    for row in xrange(table.nrows):

        value = table.row_values(row)
        
        for i, item in enumerate(value):
            try:
                value[i] = item.encode('utf-8')
            except:
                value[i] = item
        
        rows.append(value)
    rows = rows[1:]
    return rows

#获取院校数据
def getYXInfo(FILE_YX):

    rows = []

    data  = xlrd.open_workbook(FILE_YX)

    table = data.sheets()[0]

    for row in xrange(table.nrows):

        value = table.row_values(row)
        
        for i, item in enumerate(value):
            try:
                value[i] = item.encode('utf-8')
            except:
                value[i] = item
        
        rows.append(value)
    rows = rows[1:]
    return rows


def handle(rows):
    
    for row in rows:
        row[0] = str(int(row[0]))
        row[5] = str(int(row[5]))
        row[6] = str(int(row[6]))
        row[7] = str(int(row[7]))
        row[8] = str(int(row[8]))
        row[9] = str(int(row[9]))
        row[10] = str(int(row[10]))
        row[11] = str(int(row[11]))
        row[12] = str(int(row[12]))

        row[1] = row[1].encode('utf-8')
        row[2] = row[2].encode('utf-8')
        row[3] = row[3].encode('utf-8')
        try:
            row[4] = str(int(row[4]))
            
        except:
            row[4] = row[4].encode('utf-8')
        #print row
       # break
    return row
