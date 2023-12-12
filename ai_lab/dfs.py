graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

def dfs(start,goal):
    visited = list()
    stack = [[start,[]]]

    while stack:
        print(f"stack: {stack}")
        print(f"Visited: {visited}")
        print("-------------------------------------------")
        
        current,path = stack.pop()

        if current == goal:
            print(f"Goal reached and path : {path + [current]}")
            return 
        
        if current not in visited:
            visited.append(current)
            neighbours = graph.get(current)

            for i in neighbours:
                if i not in visited:
                    stack.append([i,path+[current]])
    
    print(f"No path found from {current} to {goal}")
    return

dfs('A','H')