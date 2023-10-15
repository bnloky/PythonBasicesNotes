try:
    print(10/0)
except NameError:                                #in this line i mentioned wrong exception, so its not going to be handle the exception.
    print("In python we cannot divde with zero")
finally:
    print('enter the value other than zero')