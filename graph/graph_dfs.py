def dfs(grpah,node,visisted= set()):
    if  node not in visisted:
        print(node)
        visisted.add(node)
        for child in graph[node]:
            dfs(grpah,child,visisted)
        
            
n =6 
ipt = [[0,1],[1,2],[2,3],[0,4],[1,3],[3,4],[2,5],[3,5]]
graph = {}
for i in range(n+1):
    graph[i] = []
for (u,v) in ipt:
    graph[u].append(v)
    graph[v].append(u)
dfs(graph,0)