adjacent_list = { 
    'S': [('A', 6), ('B', 5), ('C', 10)],
    'A': [('S', 6), ('E', 6)],
    'B': [('S', 5), ('D', 7), ('E', 6)],
    'C': [('S', 10), ('D', 6)],
    'D': [('B', 7), ('C', 6), ('F', 6)],
    'E': [('A', 6), ('B', 6), ('F', 4)],
    'F': [('E', 4), ('D', 6), ('G', 3)],
    'G': [('F', 3)],
}

heuristic = {
    'S':17,
    'A':10,
    'B':13,
    'C':4,
    'D':2,
    'E':4,
    'F':1,
    'G':0
}

class Graph:
    def __init__(self,adjacent_list):
        self.adjacent_list=adjacent_list
    
    def astar(self,start,destination):
        closed = list()
        opened = list(start)

        distance = {}
        distance[start] = 0

        parent = {}
        parent[start] = start

        while opened:
            v = None
            print(f"Open List: {opened}")
            print(f"Closed List: {closed}")
            print("------------------------------------------")

            for i in opened:
                if v == None or distance[v] + heuristic[v] > distance[i] + heuristic[i]:
                    v=i
            
            if v==None:
                print(f"No path found from source {start} to destination {destination}")
                return None
            
            if v == destination:
                path = list()

                while parent[v] != v:
                    path.append(v)
                    v=parent[v]

                path.append(start)
                path.reverse()

                print(f"Shortest path found, path:{path}")
                print(f"distance: {distance[destination]}")
                return
            
            for (i,j) in self.adjacent_list[v]:
                if i not in closed and i not in opened:
                    opened.append(i)
                    distance[i]=j+distance[v]
                    parent[i]=v
                
                else:
                    if distance[i] > j+distance[v]:
                        distance[i] = j+distance[v]
                        parent[i]=v

                        if i in closed:
                            closed.remove(i)
                            opened.append(i)
            
            opened.remove(v)
            closed.append(v)
        
        print(f"No path found from source {start} to destination {destination}")

graph1 = Graph(adjacent_list)
graph1.astar('S','G')