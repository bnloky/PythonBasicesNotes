print('1')
try:
    print(10/0)

except ZeroDivisionError as msg:
        print((10/2),msg)

print('2')