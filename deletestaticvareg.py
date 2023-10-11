class Test:
    a=10
    @classmethod
    def m1(cls):
        del cls.a

Test.m1()                         #when you delete the static variable that object not be shown in __dict__, 
print(Test.__dict__)