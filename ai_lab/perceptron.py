import numpy as np

x1 = np.array([1,1,1,0,0,0,1,1,1])
x2 = np.array([1,0,0,1,0,0,1,0,0])
x3 = np.array([1,0,0,1,0,0,1,1,1])
x4 = np.array([1,0,0,1,0,0,1,1,1])
x5 = np.array([1,1,0,0,0,1,0,1,1])
x6 = np.array([1,0,0,1,0,1,0,0,1])
x7 = np.array([1,0,0,1,0,0,1,1,1])
x8 = np.array([1,0,0,1,0,0,1,1,1])
x9 = np.array([0,1,1,1,0,0,1,1,1])
x10 = np.array([1,0,1,1,0,1,1,1,1])

# input matrix
x = np.array([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10])
# initial weights
w = np.array([-1, -1, 0, 0.5,0,1,-1,0.5,-1])
# desired matrix
d = np.array([0,0,1,1,0,0,1,1,0,0])

c=0.5
epoch = 10

for i in range(epoch):
    print(f"EPOCH {i+1}: ")
    for j in range(len(x)):
        net = np.dot(x[j],w)
        if net<=0:
            op=0
        elif net>0:
            op=1
        
        error = d[j]-op

        dw = c*error*x[j]
        w = w+dw
        print(f"W{j} : {w}")
    print("-------------------------------------")

print(f"Final weight after {epoch} EPOCH: {w}")

input = np.array([1,0,0,1,0,0,1,1,1])
net = np.dot(input,w)
if net<=0:
    op=0
elif net>0:
    op=1

print(net)
print(f"Output: {op}")