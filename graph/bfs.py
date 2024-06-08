def bfs(graph,visited):
    qeueu = []
    qeueu.append(1)
    visited[1] = qeueu
    while qeueu:
        temp = qeueu.pop()
        print(temp)
        for child in graph[temp]:
            if child not in visited:
                qeueu.append(child)
                visited[child] = True

ipt = [[0,1],[1,2],[2,3],[0,4],[1,3],[3,4],[2,5],[3,5]]
visited = {}
graph = {}
n= 6
for i in range(6):
    graph[i] = []
for (u,v) in ipt:
    graph[u].append(v)
    graph[v].append(u)
bfs(graph,visited)

