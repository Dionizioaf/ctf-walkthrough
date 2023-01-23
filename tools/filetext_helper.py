filepath = "./content.txt"

import sys

def readFile(pre,pos,filepath,output):
    file1 = open(filepath, 'r')
    Lines = file1.readlines()

    # count = 0
    if output == 'line':
        print(''.join(["{}{}{}".format(pre, line.strip(), pos).strip() for line in Lines]))
    else:
        for line in Lines:
            # count += 1
            print("{}{}{}".format(pre, line.strip(), pos))

def help():
    print('File Text Helper')
    print('-pre=.... => Inform the content to be prepend')
    print('-ape=.... => Inform the content to be apend')
    print('-out=.... => Inform the output format ')
    print('             line - All content in single line ')
    print('filepath => Path of the file to be processed')
    print('        ')
    print(' Ex: filetext_helper.py -pre=&# -ape=.  file.txt ')

if __name__ == "__main__":
    # readFile()
    execargs = sys.argv[1:]
    pre = ""
    pos = ""
    filepath = ""
    line = ""
    for key in execargs:
        if "-pre" in key:
            pre = key.replace("-pre=", "")
        elif "-ape" in key:
            pos = key.replace("-ape=", "")
        elif "-out" in key:
            line = key.replace("-out=", "")
        else:
            filepath = key

    readFile(pre,pos,filepath,line)

    # print(execargs)