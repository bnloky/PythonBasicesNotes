def f1(n):
    def f2(a,b):
        print("#"*30)
        n(a,b)
        print('#'*30)
    return f2

@f1
def f3(a,b):
    print(a + b)
f3(60 ,40)