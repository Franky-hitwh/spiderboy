#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import sys
import urllib
from selenium.webdriver.support.ui import Select
import handle_major
import traceback
import os
import socket

driver = webdriver.PhantomJS()
dr = WebDriverWait(driver,10)
url_list = []
page_list = []
#major_list = range(560,724)
#(1, 320)
#816
major_list = range(815, 817)
WL = "L"
YEAR = 13

reload(sys)
sys.setdefaultencoding( "utf-8" )

def login():

    print "Login..."
    driver.get("http://14wj.gk66.cn/login.aspx")

    driver.find_element_by_xpath('//input[@id="gz_username"]').send_keys('789449870')
    driver.find_element_by_xpath('//input[@id="gz_password"]').send_keys('019924')

    driver.get_screenshot_as_file('/home/hitnslab/Documents/spiderboy/spiderboy/spiders/img/getCode.png')

    vccode = raw_input('input verify code: ')

    driver.find_element_by_xpath('//input[@name="rand"]').send_keys(vccode)

    driver.find_element_by_xpath('//input[@name="sub"]').click()
    try:
        dr.until(lambda driver: driver.find_element_by_xpath("//p[@class='n2']"))
        print "Login success..."
    except:
        login()


def getUrlList():
    
    print "selenium ----> get url list"
    raw_input("Enter to go...")
    
    FIRST = True
    try:
        login()

        for major in major_list:
            
            if FIRST:
                fill_major_page(major)
                FIRST = False
            else:
                fill_page2(major)
            
            #url = driver.current_url
            #url_list.append(url)
            writeToFile(major)
            driver.back()

    except Exception as e:
        print traceback.format_exc()

    except KeyboardInterrupt:
        pass
    finally:
        logout()


def writeToFile(major_num):
    
    base = major_list[0]
    url = driver.current_url
    for i in range(1, 100):
        try:
            driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[3]/div[1]/a[%d]" % i).is_displayed()
        except:
            break

    if i == 1:
        print "not find more page for ", major_num
        return

    page_url = url + "&page=" + str(i)
    driver.get(page_url)
    dr.until(lambda driver: driver.find_element_by_xpath("//table[@id='tablecloth']"))
    print "find page %d for %d" % (i, major_num)

    path = "html/"+str(major_num)+"."+str(i)+".html"
    
    f = open(path, "w")
    
    f.write(driver.page_source)

    f.close()
    driver.back()


def fill_page2(major_num):

    print "fill major page %d..." % major_num
    time.sleep(1)
    
    n = 0
    while True:
        try:
            dr.until(lambda driver: driver.find_element_by_id("bz"))
            break
        except:
            time.sleep(1)
            n = n+1
            if n>5:
                break
    try:
        bz = driver.find_element_by_id("bz")
        bz.find_element_by_xpath("//option[@value='z']").click()
        time.sleep(1)
        bz.find_element_by_xpath("//option[@value='b']").click()
        dr.until(lambda driver: driver.find_element_by_id("zy_xf"))
        
        select = Select(driver.find_element_by_id("zy_xf"))
        #driver.find_element_tag_name(select.options[major_num])
        #dr.until(lambda driver: driver.find_element_by_id("zy_xf"))
        time.sleep(1)
        n = 0
        while True:
            try:
                dr.until(lambda driver: driver.find_element_by_id("zy_xf"))
                break
            except:
                time.sleep(1)
                n = n+1
                if n>10:
                    break

        select.options[major_num].click()

        driver.find_element_by_xpath('//input[@id="ImageButton1"]').click()
        dr.until(lambda driver: driver.find_element_by_xpath("//table[@id='tablecloth']"))
    except:
        fill_major_page(major_num)


def fill_major_page(major_num):

    print "Fill major page %s..." % major_num
    driver.get("http://14wj.gk66.cn/wj/zy.aspx")
    #driver.get_screenshot_as_file('fill.png')
    dr.until(lambda driver: driver.find_element_by_id("nf"))

    #year
    year = driver.find_element_by_id("nf")
    year.find_element_by_xpath("//option[@value='%d']" % YEAR).click()

    #wl
    if WL == "W":
        wl = driver.find_element_by_id("wl")
        wl.find_element_by_xpath("//option[@value='w']").click()

    #bz
    bz = driver.find_element_by_id("bz")
    bz.find_element_by_xpath("//option[@value='b']").click()

    dr.until(lambda driver: driver.find_element_by_id("zy_xf"))
    select = Select(driver.find_element_by_id("zy_xf"))
    time.sleep(5)
    select.options[major_num].click()
    #driver.find_element_by_xpath('//*[@id="zy_xf"]/option[@value="81"]').click()
    
    driver.get_screenshot_as_file('/home/hitnslab/Documents/spiderboy/spiderboy/spiders/img/getCode2.png')
    vcode = raw_input('input code2: ')

    driver.find_element_by_xpath('//input[@name="rand"]').send_keys(vcode)
    driver.find_element_by_xpath('//input[@id="ImageButton1"]').click()
    try:
        dr.until(lambda driver: driver.find_element_by_xpath("//table[@id='tablecloth']"))
    except:
        fill_major_page(major_num)


def logout():

    print "Logout..."

    driver.get_screenshot_as_file('/home/hitnslab/Documents/spiderboy/spiderboy/spiders/img/logout.png')
    driver.get("http://14wj.gk66.cn/loginout.aspx")
    driver.quit()


def getPageTotal():
    try:
        page_str = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[3]/div[1]').text
        pos1 = page_str.find('/')
        pos2 = page_str.find(u'\u9875', pos1)
        page = page_str[pos1+1:pos2]

        page = int(page)

    except ValueError:
        page = 1
        #sys.exit()
    
    return page

#FILEPATH = '/home/hitnslab/Documents/spiderboy/spiderboy/spiders/html-14-l/add/'
def getMajorFromFilename():

    major_file_list = []
    file_list = os.listdir(FILEPATH)
    for filename in file_list:
        if '.11' in filename and '~' not in filename:
            major_file = filename.split('.')[0]
            major_file_list.append(major_file)

    return major_file_list


def new_writeToFile():

    for k, url in enumerate(url_list):
        page_total = page_list[k]
        major_num = major_list[k]
        for i in range(1, page_total+1):
            page_url = url + "&page=" + str(i)
            driver.get(page_url)

            path = "temp/"+str(major_num)+"."+str(i)+".html"
            f = open(path, "w")
            f.write(driver.page_source)
            f.close()
            print "write %s to file..." % path[5:]


FILEPATH = "/home/hitnslab/Documents/spiderboy/spiderboy/spiders/temp/"
def changeCharset():

    url_list = []
    file_list = os.listdir(FILEPATH)
    print "There are %d files" % len(file_list)
    #print file_list
    for name in file_list:    

        filename = FILEPATH + name
        if '~' in filename:
            continue

        f = open(filename, "r")
        content = f.readlines()
        f.close()
        
        try:
            str1 = content[1].replace("gb2312", "utf-8")
            content[1] = str1
        except:
            print traceback.print_exc()
            print filename
        
        f = open(filename, "w")
        f.writelines(content)
        f.close()

def new():#find page after 11
    #print "selenium ----> get page after 11"
    raw_input("Enter to go...")
    Total_items = 0
    FIRST = True
    Write_Flag = False
    try:
        login()

        for major in major_list:
            
            if FIRST:
                fill_major_page(major)
                FIRST = False
            else:
                fill_page2(major)
            
            url = driver.current_url
            page = getPageTotal()
            Total_items += page
            page_list.append(page)
            url_list.append(url)
            #writeToFile(major)
            driver.back()
        
        #find page after 11
        new_writeToFile()
        Write_Flag = True
        changeCharset()
    except Exception as e:
        print traceback.print_exc()
        #new_writeToFile()

    except KeyboardInterrupt:
        #new_writeToFile()
        pass
    finally:
        print "Total items: ", Total_items
        if not Write_Flag:
            new_writeToFile()
        logout()

            
def main():
    
    #for major in getMajorFromFilename():
    #    major_list.append(int(major))
    
    #print 'major_list: ', major_list
    #raw_input('Input enter to go...')
    new()
    #getUrlList()
    #getMajorFromFilename()


if __name__ == '__main__':
    main()