def f(): 
    global s
    print(s)
    s = "Me too."
    print s


s = "I hate spam." 
f()
