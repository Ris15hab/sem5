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

def bfs(start,goal):
    visited = list()
    queue = [[start,[]]]

    while queue:
        print(f"Queue: {queue}")
        print(f"Visited: {visited}")
        print("-------------------------------------------")
        
        current,path = queue.pop(0)

        if current == goal:
            print(f"Goal reached and path : {path + [current]}")
            return 
        
        if current not in visited:
            visited.append(current)
            neighbours = graph.get(current)

            for i in neighbours:
                if i not in visited:
                    queue.append([i,path+[current]])
    
    print(f"No path found from {current} to {goal}")
    return

bfs('A','H')