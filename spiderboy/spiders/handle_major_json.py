#coding=utf-8
"""
    handle json fils
"""
import json
import re
import os


#the path which json files in
FILEPATH = "json/"

def getMajorList():
    
    file_list = os.listdir(FILEPATH)
    for filename in file_list:
        if '~' not in filename:
            json_file = open(FILEPATH + filename, "r")
            json_str = json_file.read()
            json_file.close()

            decode_json = json.loads(json_str)
            print "%s: %d" % (filename, len(decode_json))

    #metadata = json.loads(text, object_pairs_hook=OrderedDict); 
    #decode_json = json.loads(json_str, object_pairs_hook=OrderedDict)
    major_list = []
    f = open("major.txt", "w")
    for i in range(len(decode_json)):
        #print decode_json[i]['a']
        major_list.append(decode_json[i]['a'])
        f.writelines(decode_json[i]['a'] + '\n')
    f.close()
    return major_list

def getMajorTotal():
    """
        get the total majors
    """
    file_list = os.listdir(FILEPATH)
    for filename in file_list:
        if '~' not in filename:
            json_file = open(FILEPATH + filename, "r")
            json_str = json_file.read()
            json_file.close()

            decode_json = json.loads(json_str)
            print "%s: %d" % (filename, len(decode_json))


def getList():
    """
        return a major number list
    """
    f = open("major.json", "r")
    major_str = f.read()
    f.close()

    regex = r'"b":"(.*)"'
    #re_pat = re.compile(regex)
    #results = re_pat.search(major_str)
    #if results:
    #    results.groups()
    results = re.findall(major_str, regex)
    print results

def main():

    """read major.json, output to major.txt"""

    #getMajorList()
    #getList()
    getMajorTotal()


if __name__ == '__main__':
    main()

