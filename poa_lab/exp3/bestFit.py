partitions = []
flag = []
process = []

n = int(input("Enter the number of partitions in the memory:"))
for i in range(n):
    partitions.append(int(input(f"Enter the size of partition {i+1}: ")))
    flag.append(1)

p = int(input("Enter the number of process:"))
for i in range(p):
    process.append(int(input(f"Enter the size of process {i+1}: ")))

for i in range(p):
    fragmentation = 10000
    index = 10000

    for j in range (n):
        if process[i]<=partitions[j] and flag[j]==1 and fragmentation>partitions[j] - process[i]:
            fragmentation = partitions[j] - process[i]
            index = j
    
    if index == 10000:
        print(f"No partition found in memory for process {i+1}")
    else:
        print(f"Process {i+1} is allocated partition {index+1}")
        flag[index]=0