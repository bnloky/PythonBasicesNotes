try:
    x=int(input('enter the 1st value'))
    y=int(input('enter the 2nd value'))
    print(x/y)
except ZeroDivisionError as msg:
    print(msg)
except ValueError as e:
    print(e)