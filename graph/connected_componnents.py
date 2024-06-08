def dfs(graph,node,visited):
    print(node)
    visited.add(node)
    sum = 0
    for item in graph[node]:
        if item not in visited:
            sum += dfs(graph,item,visited)
    return sum+1
edge = [[1,2],[1,3],[4,5],[4,6],[7,8]]
nodes = [1,2,3,4,5,6,7,8,9]
graph = {}
ans = []
for key in nodes:
    graph[key] =[]
for (u,v) in edge:
    graph[u].append(v)
    graph[v].append(u)
visited = set()
for item in nodes:
    if item not in visited:
        temp = dfs(graph,item,visited)
        ans.append(temp)
print(ans)
        