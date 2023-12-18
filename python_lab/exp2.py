import math 

# find sqrt of a number 
def find_sqrt():
    num = int(input("Enter number: "))
    result = math.sqrt(num)
    print(f"Result: {result}")

# find area and perimeter of a rectangle
def find_area():
    length = int(input("Enter length: "))
    breadth = int(input("Enter breadth: "))
    area = length*breadth
    perimeter = 2*(length+breadth)
    print(f"Area: {area}\nPerimeter: {perimeter}")

# swapping nos
def swap():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    temp = x
    x = y
    y = temp
    print(f"X: {x}\nY: {y}")

# swapping nos without using temp
def swap_without_temp():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    x = x + y
    y = x - y
    x = x - y
    print(f"X: {x}\nY: {y}")

# Adding elements in List, Set and Tuple.
def adding_elements():
    # list
    temp1 = list()
    n = int(input("Enter the length of the list: "))
    for i in range(n):
        temp1.append(int(input(f"Enter element {i+1}: ")))
    print(f"List: {temp1}")

    # set
    temp2 = set()
    n = int(input("Enter the length of the list: "))
    for i in range(n):
        temp2.add(int(input(f"Enter element {i+1}: ")))
    print(f"Set: {temp2}")

    # tuple
    temp3 = (1,2,3,4,5)
    print(f"Tuple before adding element: {temp3}")
    n = int(input("Enter the element to be added: "))
    temp4 = list(temp3)
    temp4.append(n)
    temp3 = tuple(temp4)
    print(f"Tuple after adding element: {temp3}")

# Print the given triangle pattern using for loop.
# Enter height of pyramid: 6
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6
def pattern():
    n = int(input("Enter the height of the pyramid: "))
    for i in range(n):
        for j in range(i+1):
            print(f"{i+1}",end=" ")
        print()

# Find the factorial of a number using for loop.
def factorial():
    n = int(input("Enter the number: "))
    result = 1
    for i in range(1,n+1):
        result*=i
    print(f"Factorial of {n}: {result}")

# Print the Fibonacci sequence up to given 'n' value using for loop.
def fibonacci():
    n = int(input("Enter the length: "))
    n1 = 0
    n2 = 1
    if n == 1:
        print(n1)
    elif n == 2:
        print(f"{n1} {n2}")
    else:
        print(f"{n1} {n2}",end=" ")
        for i in range(2,n):
            temp = n2
            n2+=n1
            n1=temp
            print(f"{n2}",end=" ")
        print()

# Demonstrate 'while' loop with one example.
def demonstrate_while():
    n = int(input("Enter a number: "))
    rev = 0
    while n!=0:
        d = n%10
        rev = rev*10 + d
        n//=10
    print(f"Reversed: {rev}")

# Check whether the input number is even or odd using if...else loop.
def even_odd():
    n = int(input("Enter a number: "))
    if n%2==0:
        print("EVEN")
    else:
        print("ODD")

# Check whether the input year is leap year or not using nested if.
def leap_year():
    n = int(input("Enter year: "))
    if n%4==0:
        if n%400==0:
            print("Not a leap year")
        else:
            print("Leap year")
    else:
        print("Not a leap year")

# Demonstrate 'if...elif...else' loop with one example.
def demonstrate_if():
    n = 3+4j
    if type(n) is int:
        print("Integer")
    elif type(n) is float:
        print("Float")
    elif type(n) is str:
        print("String")
    elif type(n) is complex:
        print("Complex")
    elif type(n) is dict:
        print("Dictionary")
    elif type(n) is list:
        print("List")
    elif type(n) is set:
        print("Set")
    elif type(n) is tuple:
        print("Tuple")
    else:
        print("Other")

# Demonstrate 'continue', 'break' and 'pass' with one example each.
def demonstrate():
    n = 5

    print("Demonstrating continue:")
    for i in range(n):
        if i == 2:
            continue
        print(i)
    
    print("Demonstrating break:")
    for i in range(n):
        if i == 2:
            break
        print(i)
    
    print("Demonstrating pass:")
    for i in range(n):
        if i == 2:
            pass
        print(i)

    
# find_sqrt()
# find_area()
# swap()
# swap_without_temp()
# adding_elements()
# pattern()
# factorial()
# fibonacci()
# demonstrate_while()
# even_odd()
# leap_year()
# demonstrate_if()
# demonstrate()