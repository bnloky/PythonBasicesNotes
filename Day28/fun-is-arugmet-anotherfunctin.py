def f1(a):       #in this case fucntion is argument of the other function.
    a()  

def f2():
    print('hello')

f1(f2)