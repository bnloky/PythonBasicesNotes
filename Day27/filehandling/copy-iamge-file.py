f1=open('tree.jpg', 'rb')
f2=open('newpic.jpg', 'wb')
bytes=f1.read()
f2.write(bytes)
print("new image is created based on the old image")