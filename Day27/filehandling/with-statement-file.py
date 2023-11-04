with open("abd.txt", 'w') as f:
    f.write("this is a file \n")
    f.write("created by loky")
    print("this is file closed", f.closed)
print("this file is closed", f.closed)