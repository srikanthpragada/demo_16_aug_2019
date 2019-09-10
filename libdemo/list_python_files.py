import os

files = os.walk(r"e:\classroom\python\aug16\pythondemo")
for (dname, dirs, files) in files:
    if dname.find('.git') >= 0:
        continue

    print(f"{dname} contains {len(dirs)} directories and {len(files)} files")
    for f in files:
        if f.endswith('.py'):
            print(dname + "\\" + f)
