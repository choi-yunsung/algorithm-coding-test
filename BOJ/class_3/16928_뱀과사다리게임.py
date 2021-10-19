import sys
from collections import deque

graph = [i for i in range(101)]
N,M = map(int, sys.stdin.readline().rstrip().split())
for _ in range(N):
    x,y = map(int, sys.stdin.readline().rstrip().split())
    graph[x] = y
for _ in range(M):
    u,v = map(int, sys.stdin.readline().rstrip().split())
    graph[u] = v

dist = [-1]*101
dist[1] = 0
q = deque()
q.append(1)
while True:
    now = q.popleft()
    if graph[now] == 100:
        print(dist[100])
        break
    for i in range(1,7):
        next = graph[now]+i
        if next <= 100 and dist[next] == -1:
            dist[next] = dist[now]+1
            q.append(next)