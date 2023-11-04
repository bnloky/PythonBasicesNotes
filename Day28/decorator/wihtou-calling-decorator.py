def f1(a):                      #In this case we are not mentioning and calling the decorator so will we will get output only what we call like f3 only like hello3
    
    def f2():           
        print("hello1")
        print("hello2")
    return f2

def f3():
    print("hello3")

f3()