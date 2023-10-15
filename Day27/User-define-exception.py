class Tooyoundgexception(Exception):
    def __init__(self,arg):
        self.msg=arg

class Toooldexpcetion(Exception):
    def __init__(self, arg):
        self.msg=arg

age=int(input('enter the your cuurent age:'))

if age>60:
    raise Tooyoundgexception("your crrosed the margiage age, sorry we cant help")

elif age<18:
    raise Tooyoundgexception (" your age is too low for the marigae, wait for the some years")

else:
    print("you will get match deatails thorugh the mail")