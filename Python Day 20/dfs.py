def dfs(graph,start,visited=None):
    if visited is None:
        visited=set()
    visited.add(start)
    print(start,end=' ')
    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph,neighbour,visited)
graph={
    'A': ['B','C'],
    'B': ['A','D','E'],
    'C': ['A','F'],
    'D': ['B'],
    'E': ['B','F'],
    'F': ['C','E']
}
start_node=input("Enter start node from A to F:")
print("BFS traversal starting from node",start_node, ":")
dfs(graph,start_node)