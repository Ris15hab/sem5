# inputs : only 5 bits or else change line 66

import random

def generation_table(li,n):
    decimal = list(map(lambda x :int(x,2),li))
    fitness = list(map(lambda x : x*x,decimal))
    s = sum(fitness)
    probability = list(map(lambda x : round(x/s,3),fitness))
    avg = s/n
    expected = list(map(lambda x : round(x/avg,3),fitness))
    actual = list(map(lambda x: round(x),expected))
    return decimal,fitness,probability ,expected,actual

def crossover_gene_selection(li,actual,n):
    crossover = []
    temp = []
    index = []
    for i in range(n):
        if actual[i]==1:
            crossover.append(li[i])
        elif actual[i]>=2:
            for j in range(actual[i]-1):
                temp.append(li[i])
            crossover.append(li[i])
        elif actual[i]==0 and len(temp)!=0:
            crossover.append(temp[0])
            temp.pop(0)
        elif actual[i]==0 and len(temp)==0:
            index.append(i)
    while len(crossover)<=n and len(index)!=0:
        if len(temp)!=0:
            crossover.insert(index[0],temp[0])
            temp.pop(0)
            index.pop(0)
        else:
            crossover.insert(index[0],li[index[0]])
            index.pop(0)
    return crossover
            
def crossover_point(x):
    count  =0
    for i in range(len(x)):
        if x[i]=='1':
            count+=1
    return count

def perform_crossover(li,n):
    crossover = []
    for i in range(0,n,2):
        temp1 = li[i]
        temp2 = li[i+1]
        point = crossover_point(temp1)
        print(f"the crossover point for the pair {i} is : {point}")
        temp3 = temp1[point:]
        temp4 = temp2[point:]
        temp1 = temp1[0:point]+temp4
        temp2 = temp2[0:point]+temp3
        crossover.append(temp1)
        crossover.append(temp2)
    return crossover

def perform_mutation(li,n):
    mutation = []
    for i in range(n):
        index = random.randint(0,4)
        print(f"for the gene , the bit to be changed is : {index}")
        temp = li[i]
        if temp[index]=='1':
            temp = temp[0:index]+'0'+temp[index+1:]
        else:
            temp = temp[0:index]+'1'+temp[index+1:]
        mutation.append(temp)
    return mutation

m = int(input("Enter the number of generations to be computed: "))
n = int(input("Enter the number of the samples: "))
sample = list()
for i in range(n):
    sample.append(input(f"Enter Gene {i}: "))

crossed = sample.copy()
for i in range(m):
    decimal,fitness,probability,expected,actual = generation_table(crossed,n)
    if sum(actual)<n:
        max = max(actual)
        index = actual.index(max-1)
        actual[index] +=1
    if sum(actual)>n:
        max = max(actual)
        index = actual.index(max)
        actual[index] +=1
    print("\n----------------------------------------------- GENERATION ", i, "-----------------------------------------------")
    print("Initial Population\tX Value\t\tFitness Value\tProbability\tExpected Count\t\tActual Count")
    for j in range(n):
        print(f"{crossed[j]}\t\t\t{decimal[j]}\t\t\t{fitness[j]}\t\t{probability[j]}\t\t{expected[j]}\t\t{actual[j]}")
    crossover_selected = crossover_gene_selection(crossed,actual,n)
    print(f"\nGenes selected for next phase crossover:\n{crossover_selected}\n")
    crossover = perform_crossover(crossover_selected,n)
    print(f"\nGenes after performing crossover:\n{crossover}\n")
    crossed = perform_mutation(crossover,n)
    print(f"\nGenes after performing mutation:\n{crossed}\n")


decimal,fitness,probability,expected,actual = generation_table(crossed,n)
print("\n-----------------------------------------------FINAL-----------------------------------------------")
print("Initial Population\tX Value\t\tFitness Value\tProbability\tExpected Count\t\tActual Count")
for j in range(n):
    print(f"{crossed[j]}\t\t\t{decimal[j]}\t\t\t{fitness[j]}\t\t{probability[j]}\t\t{expected[j]}\t\t{actual[j]}")