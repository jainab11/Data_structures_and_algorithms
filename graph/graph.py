ipt = [[0,1],[1,2],[2,3],[0,4],[1,3],[3,4],[2,5],[3,5]]
nodes = 6
matrix = []

graph = {}
for i in range(6):
    graph[i] = []
for (u,v) in ipt:
    graph[u].append(v)
    graph[v].append(u)
    
for item in graph.items():
    print(item)
# for i in range(6):
#     temp = []
#     for j in range(6):
#         temp.append(0)
#     matrix.append(temp)
# for (u,v) in ipt:
#     matrix[u][v] = 1
#     matrix [v][u] = 1
    
# for item in matrix:
#     print(item)