#                 S(17)
#              /    |     \
#         v(6)/  (5)|      \(10)    
#         A(10)    B(13)    C(4)
#          \     /     \      /
#       (6) \   /(6) (7)\    /(6)
#            E(4)       D(2)
#              \         /
#            (4)\       /(6)
#                \     /
#                  F(1)
#                   |(3)
#                  G(0)

# (neighbour,level)
adjacent_list = { 
    'S': [('A', 1), ('B', 1), ('C', 1)],
    'A': [('S', 0), ('E', 2)],
    'B': [('S', 0), ('D', 2), ('E', 2)],
    'C': [('S', 0), ('D', 2)],
    'D': [('B', 1), ('C', 1), ('F', 3)],
    'E': [('A', 1), ('B', 1), ('F', 3)],
    'F': [('E', 2), ('D', 2), ('G', 4)],
    'G': [('F', 3)],
}

heuristic = {
    'S':17,
    'A':10,
    'B':13,
    'C':4,
    'D':2,
    'E':4,
    'F':5,
    'G':0
}


def hillClimbing(start,start_depth):
    queue = [[start,[],start_depth]]
    closed = []
    temp = []

    while queue:
        print(f"Queue: {queue}")
        print(f"Closed: {closed}")
        print("-------------------------------------------")

        temp = queue.copy()
        current , path , level = queue.pop()
        queue.clear()

        heu = heuristic.get(current)
        closed.append(current)
        
        for (i,j) in adjacent_list[current]:
            if i not in closed:
                closed.append(i)
            if j==level+1 and heuristic[i]<heu:
                if len(queue)==0:
                    queue.append([i,path+[current],level+1])
                    closed.remove(i)
                else:
                    if heuristic[i]< heuristic[queue[0][0]]:
                        closed.append(queue[0][0])
                        queue.pop()
                        queue.append([i,path+[current],level+1])
                        closed.remove(i)
    
    print(f"Final Node reached: {temp[0][0]}\nLevel: {temp[0][2]}\nPath: {temp[0][1]}\nMin Heuristic:{heuristic[temp[0][0]]}")
        
hillClimbing('S',0)     