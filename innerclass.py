class Car:
    def __init__(self):
        print('this is the outer class with name car')
        
    class Engine:
        def __init__(self):
         print('this is a innerclasss wiht name engine')

        def m1 (self):
         print('this ford car comeup with dargon engine ')

ford=Car()
dargon=ford.Engine()
dargon.m1()