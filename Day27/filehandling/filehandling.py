f=open("abc.txt", 'w')

print("name of the file", f.name)
print("mode of the file", f.mode)
print(f.readable)
print(f.writable)
print(f.closed)
f.close()
print(f.closed)