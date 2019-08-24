def wish(*names, msg="Hi"):
    for n in names:
        print(msg, n)


wish("Bill",10,True)
wish("Bill", "Larry", msg="Hello")
