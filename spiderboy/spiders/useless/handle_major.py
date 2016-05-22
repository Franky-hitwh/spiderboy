#coding=utf-8
import json

def getMajorList():
    
    print "handle_major ----> get major list from major.txt"
    raw_input('Enter to go...')
    return readMajorFile()


def readMajorFile():

    f = open("major.txt", "r")
    
    major_list = f.readlines()
    
    temp_list = []
    
    for major in major_list:
        temp_list.append(major.replace("\n", ""))
    
    major_list = temp_list

    return major_list

def main():
    print getMajorList()[0:10]


if __name__ == '__main__':
    main()

