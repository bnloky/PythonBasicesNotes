print('1')
# print(20/0)
try:
    print(10/2)
except ZeroDivisionError as msg:
    print(msg)
finally:
    print('2')


print("hello")
