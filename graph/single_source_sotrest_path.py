def sssp(graph,visited,distanca):
    que = []
    que.append(1)
    visited[1] = que
    distanca[1] = 0
    while que:
        temp = que.pop()
        print(temp)
        for child in graph[temp]:
            if child not in visited:
                que.append(child)
                visited[child] = True
                distanca[child] = distanca[temp]+1
        print(distanca)
        
        
n = 6 
ipt = [[0,1],[1,2],[2,3],[0,4],[1,3],[3,4],[2,5],[3,5]]
graph = {}
visited ={}
distance = []
for i in range(n):
    graph[i] = []
for (u,v) in ipt:
    graph[u].append(v)
    graph[v].append(u)
sssp(graph,visited,distance)
