class Test:
    def m1(self):
        a=1000
        print(a)

    def m2(self): 
        b=2000
        print(a)     #we get a error becasue we use m1 method "a" vairable here, its a localvairable its scope only within method. 
        print(b)

t=Test()
t.m1()
t.m2()