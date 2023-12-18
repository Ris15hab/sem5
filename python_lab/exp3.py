# list functions
def list_functions():
    temp1 = [1,2,3]
    print(f"Initial list: {temp1}")
    temp1.append(4)
    print(f"append(4): {temp1}")
    temp2 = temp1.copy()
    print(f"copy(): {temp2}")
    temp2.clear()
    print(f"clear(): {temp2}")
    print(f"count(1): {temp1.count(1)}")
    temp1.extend([4,5])
    print(f"extend([4,5]): {temp1}")
    print(f"index(4): {temp1.index(4)}")
    temp1.insert(1,8)
    print(f"insert(1,8): {temp1}")
    temp1.pop()
    print(f"pop(): {temp1}")
    temp1.remove(4)
    print(f"remove(4): {temp1}")
    temp1.reverse()
    print(f"reverse: {temp1}")
    temp1.sort()
    print(f"sort(): {temp1}")

# tuple functions 
def tuple_functions():
    temp1 = (1,2,3,4)
    print(f"Inital tuple: f{temp1}")
    print(f"count(1): {temp1.count(1)}")
    print(f"index(1): {temp1.index(1)}")

# set functions
def set_functions():
    temp1 = {1,2,3,4}
    print(f"Initial set: {temp1}")
    temp1.add(5)
    print(f"add(5): {temp1}")
    temp2 = temp1.copy()
    print(f"copy(): {temp2}")
    temp2.clear()
    print(f"clear(): {temp2}")
    temp2 = {3,4,5,6,7}
    print(f"difference: {temp1.difference(temp2)}")
    print(f"intersection: {temp1.intersection(temp2)}")
    print(f"union: {temp1.union(temp2)}")
    temp1.pop()
    print(f"pop(): {temp1}")
    temp1.discard(3)
    print(f"discard(3): {temp1}")

# dictionary functions
def dict_functions():
    temp1 = {
        1:'a',
        2:'b',
        3:'c'
    }
    print(f"Initial dict: {temp1}")
    temp2 = temp1.copy()
    print(f"copy(): {temp2}")
    print(f"keys(): {temp1.keys()}")
    print(f"values(): {temp1.values()}")
    temp1.pop(1)
    print(f"pop(1): {temp1}")
    print(f"get(2): {temp1.get(2)}")
    print(f"items: {temp1.items()}")
    temp1.clear()
    print(f"clear(): {temp1}")

# histogram
def histogram(x):
    items = {}
    for i in x:
        if i in items.keys():
            items[i]+=1
        else:
            items[i] = 1
    item = list(items.keys())
    freq = list(items.values())
    for i in range(len(item)):
        for j in range(i,len(item)):
            if freq[i]>freq[j]:
                temp = item[i]
                item[i] = item[j]
                item[j] = temp
                temp = freq[i]
                freq[i] = freq[j]
                freq[j]=temp
            elif freq[i]==freq[j] and item[i]>item[j]:
                temp = item[i]
                item[i] = item[j]
                item[j] = temp
                temp = freq[i]
                freq[i] = freq[j]
                freq[j]=temp
    print("[",end="")
    for i in range(len(item)):
        print(f"({item[i]},{freq[i]})",end=",")
    print("]")

# perfect number
def perfect_number():
    n = int(input("Enter Number:"))
    result = 0
    for i in range(1,n):
        if n%i==0:
            result+=i
    if(n==result):
        print("PERFECT NUMBER")
    else:
        print("NOT A PERFECT NUMBER")

# tower of hanoi
def tower_of_hanoi(n,source,auxillary,target):
    if n==1:
        print(f"MOVE DISK 1 FROM PEG {source} to PEG {target}")
        return
    tower_of_hanoi(n-1,source,target,auxillary)
    print(f"MOVE DISK {n} FROM PEG {source} to PEG {target}")
    tower_of_hanoi(n-1,auxillary,source,target)

# lambda to find greater of 2 numbers
def greater():
    num1 = int(input("Number1: "))
    num2 = int(input("Number2: "))
    maximum = lambda a,b: a if a>b else b
    print(f"MAX: {maximum(num1,num2)}")

# Using map function perform element wise addition of elements of two lists.
def addition_using_map():
    temp1 = [1,2,3,4,5]
    temp2 = [3,4,5,6,7]
    temp3 = list(map(lambda a,b: a+b ,temp1,temp2))
    print(temp3)

# Using map and filter find the cube of all the odd numbers from the given input list
def map_filter():
    temp1 = [1,2,3,4,5,6,7,8,9]
    print(list(map(lambda x: x*x*x, filter(lambda y: y%2!=0,temp1))))
    
# list_functions()
# tuple_functions()
# set_functions()
# dict_functions()
# print("Enter element:")
# histogram(list(map(int,input().split())))
# perfect_number()
# tower_of_hanoi(int(input("Enter the number of disks:")),'A','B','C')
# greater()
# addition_using_map()
# map_filter()