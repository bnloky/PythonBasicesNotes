f=open("file.sh",'w')

f.write("name \n")
f.write("surname \n")
f.write("age \n")
f.write("address")
print("this file is closed", f.closed)
f.close()
print(f.closed)