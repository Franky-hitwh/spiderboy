"""
    privode api
"""

import os
import traceback
import new_exmodule

#html dir
FILEPATH = "/home/hitnslab/Documents/spiderboy/spiderboy/spiders/temp/"


#add 'file://' to FILEPATH to build url
URL_PRE = 'file://' + FILEPATH
#URL_PRE = "file:///home/hitnslab/Documents/spiderboy/spiderboy/spiders/temp/"

def getLocalUrl():    #return a url list of local file
    
    url_list = []
    file_list = os.listdir(FILEPATH)
    print "There are %d files" % len(file_list)
    for filename in file_list:
        
        if '~' in filename:
            continue

        url = URL_PRE + filename
        
        url_list.append(url)

    return url_list


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

def main():
    #changeCharset("/home/hitnslab/Documents/spiderboy/spiderboy/spiders/html/1.3.html")
    changeCharset()

    #new_exmodule.main()
    #return getLocalUrl()


if __name__ == '__main__':
    main()
