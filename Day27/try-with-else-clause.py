# Program to depict else clause with try-except 
# Python 3 
# Function which returns a/b 
def method(a , b): 
	try: 
		c = ((a+b) / (a-b)) 
	except ZeroDivisionError: 
		print ("a/b result in 0") 
	else: 
		print (c) 

# Driver program to test above function 
method(2.0, 3.0) 
method(3.0, 3.0) 
