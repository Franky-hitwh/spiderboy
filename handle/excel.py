#coding=utf-8

import xlrd
import xlwt
from datetime import datetime
import sys
from xlwt import *
import info
import traceback

reload(sys)
sys.setdefaultencoding( "utf-8" )

FINALFILE = "dir/2015_w.xls"
FILE_READ = '2015-w.xlsx'
FILE_YX = 'yx_info.xls'
FILE_XK = "xk_info.xls"
FILE_Zy_Xw = "zy_xw.xlsx"
FILE_Zy_Yx = "2015_w_zy&yx.xls"

def writeToExcel(rows):
    #k = [20, 21, 22, 23, 24, 25, 26, 27, 28]
    #xk_list = ["一级国家重点学科", "二级国家重点学科", "一级国家重点(培育)学科", "二级国家重点(培育)学科", "一级学科博士/硕士点", "二级学科博士/硕士点", "一级学科硕士点", "二级学科硕士点"]

    w = Workbook(encoding='utf-8')
    ws = w.add_sheet('xlwt was here')

    for i, row in enumerate(rows):
        #for j, cell in enumerate(row):
        j = 0
        while j < len(row):
            cell = row[j]
            try:
                if type(cell) == type([]):
                    ws.write(i, cell[0], cell[1])
                else:
                    ws.write(i, j, cell)
            except:
                print cell
                print traceback.print_exc()
                print "i = ", i
                break
                
            j = j+1
            
    w.save(FINALFILE)


def link_yx(rows, yxs):

    for row in rows:    #link two tables: zy & xx
        for yx in yxs:
            if row[3] == yx[0]:
                row.extend(yx)
                #print row
                break       #only extend once

    return rows

def getYjxk(zy_xws, temp_row_zy):

    for zy_xw in zy_xws:

        if temp_row_zy == zy_xw[3]:         #through zy contact two tables:zy & zy_xw
            return zy_xw[5]                #get zy--yjxk from zy_xw

def handle(xk):
    #15, 6
    k = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    xk_list = ["一级国家重点学科", "二级国家重点学科", "一级国家重点(培育)学科", "二级国家重点(培育)学科", "一级学科博士/硕士点", "二级学科博士/硕士点", "服务","一级学科硕士点",  "二级学科硕士点"]
    for i, item in enumerate(xk_list):
        if xk[1] in item:
            return [k[i], xk[2]]
    #print "not match:", xk[2]

    return [k[9], xk[2]]


def handle2(xk_list):

    result = []
    temp = []
    
    for l1 in xk_list:
        if l1[0] not in temp:            
            result.append(l1)
            temp.append(l1[0])
        else:
            for l2 in result:
                if l1[0] == l2[0]:
                    l2[1] += ', ' + l1[1]
                    #print l2[1]

    return result



def link_xk(rows, zy_xws, xks):

    for row in rows:
        temp_row_zy = row[2].split('（')[0]    #zy, not contains the content in ()
        temp_row_xx = row[3]    #xx

        yjxk = getYjxk(zy_xws, temp_row_zy)

        xk_list = []
        for xk in xks:                      #find all zy&xx from xk_info table
              
            temp_xk_xx = xk[3]              #xx
            temp_xk_yjxk = xk[5]            #xkzy
            temp_xk_rank = xk[1]

            if temp_xk_yjxk == yjxk and temp_xk_xx == temp_row_xx:  #through xx and yjxk locate one item in xk_info table

                temp = handle(xk)
                #try:
                #    print temp[0], temp[1]
                #except:
                #    pass
                if temp:
                    xk_list.append(temp)

        if len(xk_list) != 0:
            #print len(xk_list)
            xk_list = handle2(xk_list)

            #for item in xk_list:
                #print item[0], item[1]

            row.extend(xk_list)

        #break
    return rows

READ_FROM = '2013_w_zy&yx.xls'
def write_zy_yx(rows):
    w = Workbook(encoding='utf-8')
    ws = w.add_sheet('xlwt was here')

    for i, row in enumerate(rows):
        for j, cell in enumerate(row):
            ws.write(i, j, cell)

    w.save(READ_FROM)


def create_zy_yx():
    rows = info.getRows(FILE_READ)
    yxs = info.getYXInfo(FILE_YX)
    rows = link_yx(rows, yxs)
    #write_zy_yx(rows)
    return rows


def main():

    rows = create_zy_yx()
    #rows = info.getZyYxInfo(FILE_Zy_Yx)
    xks = info.getXkInfo(FILE_XK)
    zy_xws = info.getZyXwInfo(FILE_Zy_Xw)
    

    #rows = link_yx(rows, yxs)
    
    rows = link_xk(rows, zy_xws, xks)
                
    writeToExcel(rows)


if __name__ == '__main__':

    main()
























