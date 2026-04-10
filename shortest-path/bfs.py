from collections import deque

def bfs(graph,start,goal):
    queue=deque([[start]])
    visited={start}
    while queue:
        path=queue.popleft()
        node=path[-1]

        if node==goal:
            return path
    
        for neighbor in graph.get(node,[]):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path+[neighbor])
    return None

n=int(input("Enter the number of nodes: "))
graph={input(f"Node {i+1}: "): [] for i in range(n)}

e=int(input("Enter the number of edges: "))
for i in range(e):
    u,v=input(f"Edge{i+1}: ").split()
    graph[u].append(v)
    graph[v].append(u)

start,goal=input("Start Node: "),input("Goal Node: ")
path=bfs(graph,start,goal)

if path:
    print(f"Path: {'->'.join(path)}\n Length: {len(path)-1}")
else:
    print("No path found.")