import os
import sys

# usage : python search_files.py  pattern folder

if len(sys.argv) == 1:
    print("Usage : python search_files.py pattern [folder]")
    sys.exit(0)

if len(sys.argv) < 3:
   startfolder = os.getcwd()
else:
   startfolder = sys.argv[2]  # folder to start with

files = os.walk(startfolder)

pattern = sys.argv[1]  # pattern to search for

for (dname, dirs, files) in files:
    for f in files:
        if f.find(pattern) >= 0:
            print(dname + "\\" + f)
