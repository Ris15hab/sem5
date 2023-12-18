# Data Types

# string 
x = "rishab"
print(type(x))

# integer
x = 5
print(type(x))

# float
x = 5.5
print(type(x))

# complex
x = 2 +5j
print(type(x))

# list
x = [1,2,3]
print(type(x))

# range
x =  range(3)
print(type(x))

# tuple
x = (1,2,3)
print(type(x))

# dictionary 
x = {1:'a',2:'b'}
print(type(x))

# set
x = {1,2,3}
print(type(x))

# boolean 
x =True
print(type(x))

# binary 
x = b"rishab"
print(type(x))

# none
x = None
print(type(x))

# Operators

# Arithmetic Operators
x = 6
y = 2
print(f"x+y= {x+y}")
print(f"x-y= {x-y}")
print(f"x*y= {x*y}")
print(f"x/y= {x/y}")
print(f"x%y= {x%y}")
print(f"x**y= {x**y}")
print(f"x//y= {x//y}")

# Assignment 
x = 2
print(x)

x+= 2
print(f"x+= {x}")

x-= 2
print(f"x-= {x}")

x*= 2
print(f"x*= {x}")

x/= 2
print(f"x/= {x}")

x%= 2
print(f"x%= {x}")

x**= 2
print(f"x**= {x}")

x//= 2
print(f"x//= {x}")

# Comparison 
x=2
y=2
print(f"x==y: {x==y}")
print(f"x!=y: {x!=y}")
print(f"x>y: {x>y}")
print(f"x<y: {x<y}")
print(f"x>=y: {x>=y}")
print(f"x<=y: {x<=y}")

# Logical
x = 5
y = 10
print("and :",x>5 and y>5)
print("or :",x>5 or y>5)
print("not :",not x>5)

# Identity
x = 2
y = "2"
print("x is y: ",x is y)
print("x is not y: ",x is not y)

# Membership
lst = [1,2,3]
x = 2
print ("x in list: ",x in lst)
print ("x not in list: ",x not in lst)

# Bitwise
x = 10
y = 5
print(f"and : {x&y}")
print(f"or : {x|y}")
print(f"xor : {x^y}")
print(f"not : {~x}")
print(f"zero fill left shift : {x<<2}")
print(f"signed right shift : {x>>2}")