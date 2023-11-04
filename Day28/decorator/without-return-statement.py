def print_something(s):
    print('Printing::', s)


output = print_something('Hi')

print(f' {output}')

print(id(print_something))
print(id(output))
print(type(output))