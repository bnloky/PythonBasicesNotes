def star(func):
    def inner(*args, **kwargs):
        print("*" * 100)
        func(*args, **kwargs)
        print("*" * 50)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 50)
        func(*args, **kwargs)
        print("%" * 50)
    return inner


@star
@percent
def printer(msg):
    print(msg)

printer("Hello")