def f1(a):               #In this case we are mentioned the decorator(@f1) so its return the f2 values and decorator calling from the f3 funtion 
    def f2():             #here we declare the decorator on the top of the f3 function so f3 we call decorator and its output of the f1 not of the f3.
        print("hello1")
        print("hello2")

    return f2
@f1                    #decorator is the funciton which executed when someone function is invoked and its define top of that function.
def f3(): 
    print("hello3")
f3()