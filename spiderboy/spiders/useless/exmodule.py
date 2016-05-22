#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver import ActionChains
import time
import sys
import urllib
from selenium.webdriver.support.ui import Select
import pytesseract
from PIL import Image
import handle_major

import traceback
#Select(driver.find_element_by_id("gender")).select_by_index(1)

driver = webdriver.PhantomJS()
dr = WebDriverWait(driver,10)
url_list = []
page_list = []
major_list = range(1, 20)

WL = "W"

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
    except:
        login()


def fill_major_page(major_num):

    print "Fill major page %d..." % major_num
    driver.get("http://14wj.gk66.cn/wj/zy.aspx")
    #driver.get_screenshot_as_file('fill.png')
    dr.until(lambda driver: driver.find_element_by_id("nf"))

    #year
    year = driver.find_element_by_id("nf")
    year.find_element_by_xpath("//option[@value='15']").click()

    #wl
    if WL == "W":
        wl = driver.find_element_by_id("wl")
        wl.find_element_by_xpath("//option[@value='w']").click()

    #bz
    bz = driver.find_element_by_id("bz")
    bz.find_element_by_xpath("//option[@value='b']").click()

    dr.until(lambda driver: driver.find_element_by_id("zy_xf"))
    #dr.until(lambda driver: driver.find_element_by_xpath("option[@value=%s]" % major_num))
    

    #zy = driver.find_element_by_id("zy_xf")
    #zy.find_element_by_xpath("option")[major_num].click()
    select = Select(driver.find_element_by_id("zy_xf"))
    time.sleep(3)
    select.options[major_num].click()
    #driver.find_element_by_xpath('//*[@id="zy_xf"]/option[@value="310"]').click()
    
    driver.get_screenshot_as_file('/home/hitnslab/Documents/spiderboy/spiderboy/spiders/img/getCode2.png')
    #im = Image.open("/home/hitnslab/Documents/spiderboy/spiderboy/spiders/img/getCode2.png")
    #box = (359,832,415,870)
    #i = im.crop(box).show()
    vcode = raw_input('input code2: ')

    driver.find_element_by_xpath('//input[@name="rand"]').send_keys(vcode)
    driver.find_element_by_xpath('//input[@id="ImageButton1"]').click()
    try:
        dr.until(lambda driver: driver.find_element_by_xpath("//table[@id='tablecloth']"))
    except:
        fill_major_page(major_num)
    #time.sleep(1)


def fill_page2(major_num):

    print "fill major page %d..." % major_num
    #time.sleep(4)
    dr.until(lambda driver: driver.find_element_by_id("bz"))

    bz = driver.find_element_by_id("bz")

    bz.find_element_by_xpath("//option[@value='z']").click()
    bz.find_element_by_xpath("//option[@value='b']").click()
    dr.until(lambda driver: driver.find_element_by_id("zy_xf"))
    
    select = Select(driver.find_element_by_id("zy_xf"))
    #driver.find_element_tag_name(select.options[major_num])
    dr.until(lambda driver: driver.find_element_by_id("zy_xf"))
    time.sleep(5)
    """if major_num > 298:
        time.sleep(5)
    elif major_num > 40:
        time.sleep(3)
    else:
        time.sleep(2)"""
    #driver.find_element_by_xpath('//options[@value="310"]').click()
    select.options[major_num].click()

    driver.find_element_by_xpath('//input[@id="ImageButton1"]').click()
    dr.until(lambda driver: driver.find_element_by_xpath("//table[@id='tablecloth']"))


def writeToFile(major):

    html = driver.page_source

    f = open("html/"+str(major)+".html", "w")
    f.write(html)
    f.close()

    for i in range(12, 100):
        try:
            driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[3]/div[1]/a[%d]" % i).is_displayed()
        except:
            break
    page_list.append(i+1)
    #print page_list
    #[9, 1, 1, 1, 2, 1, 1, 8, 1, 1, 2, 4, 1, 11, 1, 4, 2, 1, 2, 9, 1, 1, 3, 1, 11, 3, 2, 2, 1, 11, 1, 3, 1]


def writeToFile2(major, i):
    
    path = "html/"+str(major)+"."+str(i)+".html"
    
    f = open(path, "w")
    
    f.write(driver.page_source)

    f.close()

    for i in range(1, 100):
        try:
            driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[3]/div[1]/a[%d]" % i).is_displayed()
        except:
            break
    page_list.append(i+1)


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
            
            url = driver.current_url
            url_list.append(url)
            #origin func
            writeToFile(major)

            #print driver.current_url
            driver.back()
            #print driver.current_url
            #import pdb
            #pdb.set_trace()
            #time.sleep(2)
            #dr.until(lambda driver: driver.find_element_by_id("bz"))

        find_more_page()

    except Exception as e:
        print e
        #print "Error in exmodule..."
        print traceback.format_exc()
        print page_list
        find_more_page()
        sys.exit()
    except KeyboardInterrupt:
        find_more_page()
    
    finally:
        
        logout()


def getPage(k):

    return page_list[k]


def find_more_page():

    base = major_list[0]
    for k, url in enumerate(url_list):

        total_page = getPage(k)
        print 'total_page: ', total_page

        if total_page == 2 or total_page == 1:
            continue

        for i in range(total_page-1, total_page):#2

            page_url = url + "&page=" + str(i)

            driver.get(page_url)
                
            dr.until(lambda driver: driver.find_element_by_xpath("//table[@id='tablecloth']"))
                
            print "find page %d for %d" % (i, k + base)
            writeToFile2(k + base, i)


def getCookies():
    
    return driver.get_cookies()


def logout():
    
    print "Logout..."
    driver.get_screenshot_as_file('/home/hitnslab/Documents/spiderboy/spiderboy/spiders/img/logout.png')
    driver.get("http://14wj.gk66.cn/loginout.aspx")
    driver.quit()


def main():

    getUrlList()


if __name__ == '__main__':
    main()
    #print driver.current_url

    #time.sleep(2)
    #driver.get_screenshot_as_file('dest.png')

    #get vccode png
    #element = driver.find_element_by_id("checkCode")
    #urllib.urlretrieve('http://14wj.gk66.cn/ashx/codewj.ashx' ,'test.ashx')
    #image = Image.open('test.ashx')
    #vcode = pytesseract.image_to_string(image)
    #print vcode
