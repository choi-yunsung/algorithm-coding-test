import sys
from collections import deque

n,m = map(int, sys.stdin.readline().strip().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    q = deque()
    q.append([0,0,1])
    visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1

    while q:
        x,y,wall = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][wall]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and wall == 1:
                    visited[nx][ny][0] = visited[x][y][wall] + 1
                    q.append([nx,ny,0])
                elif graph[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    q.append([nx,ny,wall])
    return -1

print(bfs())