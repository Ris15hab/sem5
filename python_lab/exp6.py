n = input("Enter numbers: ")
with open ('./test.txt','w') as f1:
    f1.write(n)

with open ('./test.txt','r') as f1:
    data = f1.read()
    numbers = list(map(lambda x: int(x),data.split()))

sorted_list = numbers.sort()
max_list= max(numbers)
min_list = min(numbers)
sum_list= sum(numbers)
length = len(numbers)
avg = sum_list/length

with open('./test.txt','w') as f1:
    f1.write(f"\nList: {numbers}")
    f1.write(f"\nSorted List: {sorted_list}")
    f1.write(f"\nMaximum : {max_list}")
    f1.write(f"\nMinimum : {min_list}")
    f1.write(f"\nSum : {sum_list}")
    f1.write(f"\nAverage : {avg}")
    f1.close()
    print("file updated...")