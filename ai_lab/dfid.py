graph = {
    'A' : ['B' , 'C'],
    'B' : ['A' , 'D' , 'E'],
    'C' : ['A' , 'F' , 'G'],
    'D' : ['B'],
    'E' : ['B' , 'H'],
    'F' : ['C'],
    'G' : ['C'],
    'H' : ['E']
}

def dfid(start,goal,limit):
    stack = [[start,[],0]]
    visited = []
    while stack:
        print(f"Stack: {stack}")
        print(f"Visited: {visited}")
        print("---------------------------------------------")

        current , path , depth= stack.pop()

        if current == goal:
            print(f"Goal Reached , path: {path+[current]}, at limit: {limit} iteration")
            return True
        
        if current not in visited and depth<limit:
            neighbours = graph[current]
            for i in neighbours:
                if i not in visited:
                    stack.append([i,path+[current],depth+1])
        visited.append(current)
        
        
    print(f"No path found from source {start} to goal {goal} at level {limit}")
    return False

def dfid_driver(start,goal):
    count = 0
    while True:
        result = dfid(start,goal,count)
        if result:
            return
        else:
            count+=1

dfid_driver('A','H')