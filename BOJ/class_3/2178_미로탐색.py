import sys
from collections import deque

N,M = map(int, sys.stdin.readline().rstrip().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = [[False]*M for _ in range(N)]
q = deque([(0,0,1)])
while q:
    x,y,cnt = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            if visited[nx][ny]:
                continue
            if nx == N-1 and ny == M-1:
                print(cnt+1)
                q.clear()
                break
            if graph[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx,ny,cnt+1))