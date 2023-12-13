from BTrees._IIBTree import IIBTree
import timeit

btree = IIBTree()

while True:
    choice = int(input("Enter\n1.Insert Value in Btree\n2.Search element in Btree\n3.Print BTree\n4.Delete an element\n0.Exit:\n"))
    if choice ==1:
        value = int(input("Enter the value to be inserted in btree: \n"))
        btree[value] = value
        print("Value inserted!")
    elif choice ==2:
        value = int(input("Enter the value to be searched in btree: \n"))
        start_time = timeit.default_timer()
        if value in btree:
            print("Element if found in btree.")
        else:
            print("Element not present in the btree")
        end_time = timeit.default_timer()
        print(f"Time of search: {round((end_time-start_time)*1000 , 3)} milliseconds")
    elif choice == 3:
        for value in btree:
            print(f"value: {value}")
    elif choice == 4:
        value = int(input("Enter the value to be deleted from btree: \n"))
        try:
            del btree[value]
            print("Value deleted from the btree")
        except:
            print("Value not present in the btree")
    elif choice == 0:
        print("Exiting...")
        break
    else:
        print("Invalid input")