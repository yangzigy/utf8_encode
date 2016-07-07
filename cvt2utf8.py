#!/usr/local/bin/python3

import chardet
import sys
import os

#Config info, please change!
ext_filter = ['txt','c','cpp','h','cs','py']


def walkdir(dirname): #遍历文件夹中的每一个文件
    assert os.path.isdir(dirname)
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            extension = os.path.splitext(filename)[1][1:]
            if (extension in ext_filter):
                filename = os.path.join(root, filename)
                walkfile(filename)

def walkfile(filename): #对于一个文件
    assert os.path.isfile(filename)
    print("Opening file: {}".format(filename))
    with open(filename, 'rb') as f: # read under the binary mode
        bytedata = f.read()
        encoding = chardet.detect(bytedata)['encoding']

    if type(encoding) == None:
        print("Error: unable to recognize the file's type.")
        return

    if encoding.lower()[0:3] == 'utf':
        print("Skipped, since its type is already {}.".format(encoding))
    else:
        print ("The file was encoded in {}".format(encoding))
        strdata = bytedata.decode(encoding, 'strict')
        print("Start writing file: {} in UTF-8".format(filename))
        with open(filename, 'wb') as f: # write under the binary mode
            f.write(strdata.encode('utf-8'))
        print("End writing file: {} in UTF-8".format(filename))

def main(root_path):
    print ("Start running main()")
    if os.path.isdir(root_path):
        walkdir(root_path)
        return
    if os.path.isfile(root_path):
        walkfile(root_path)
        return
    # The file specified is neither a directory or a regular file
    errmsg = "The file specified '{}' is neither a directory or a regular file".format(root_path)
    print (errmsg)
    return

if __name__ == '__main__':
	if len(sys.argv)==2:
		main(sys.argv[1])
	else :
		print("need a param")
