import heapq

def lcfs(graph,start,goal):
    pq=[(0,start,[start])]
    visited=set()
    while pq:
        cost,node,path=heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        if node==goal:
            return cost, path

        for n,weight in graph.get(node, {}).items():
            if n not in visited:
                new=cost+weight
                heapq.heappush(pq,(new,n,path+[n]))
    return float('inf'),[]

graph_data = {
    'A': {'B': 2, 'C': 3, 'D': 4}, 'B': {'E': 4, 'F': 5},
    'C': {'J': 10}, 'E': {'F': 1}, 'F': {'G': 2}, 'G': {}
}

start='A'
goal='G'

result_cost,result_path=lcfs(graph_data,start,goal)
if result_cost==float('inf'):
    print("No path found. ")
else:
    print(f"The path from {start} to {goal} exists.")
    print(f"Length of path is {result_cost}")