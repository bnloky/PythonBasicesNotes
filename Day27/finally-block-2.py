try:
    print(10/0)
except ZeroDivisionError:
    print("In python we cannot divde with zero")
finally:
    print('enter the value other than zero')