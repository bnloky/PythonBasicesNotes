def decor(func):
    def inner(name):
        if    name=="sunny":
            print(" your not eligible")

        else: 
             func(name)
    return inner

@decor
def  vote(name):
    print("your eligble for voting ", name)

vote('suresh')
vote('lokesh')
vote('sunny')    