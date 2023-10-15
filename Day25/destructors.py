import time

class Test:
    def __init__(self):
        print('object is initialised')

    def __del__(self):
        print('I hope your fine to going for cleanup activities')

t1=Test()
t1=None                 #here object is refering to the none it means calling the garabge collection it will initalse the descructor.
time.sleep(10)          #It wait for the 10 second.
print('end of the application')