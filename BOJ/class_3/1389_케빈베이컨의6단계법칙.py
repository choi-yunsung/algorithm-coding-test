import sys
n,m = map(int, sys.stdin.readline().rstrip().split())

INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

min_kb = min([sum(g[1:]) for g in graph])
for i, g in enumerate(graph):
    if sum(g[1:]) == min_kb:
        print(i)
        break