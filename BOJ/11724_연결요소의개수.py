import sys
from collections import deque

N,M = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [False]*(N+1)

answer = 0
for i in range(1, N+1):
    if not visited[i]:
        visited[i] =True
        q = deque([i])
        while q:
            v = q.popleft()
            for u in graph[v]:
                if not visited[u]:
                    visited[u] = True
                    q.append(u)
        answer += 1
print(answer)