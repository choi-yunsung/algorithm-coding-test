import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            answer.append(1)
            graph[i][j] = 0
            q = deque([(i,j)])
            while q:
                x,y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx >= 0 and nx < N and ny >= 0 and ny < N:
                        if graph[nx][ny] == 1:
                            answer[-1] += 1
                            graph[nx][ny] = 0
                            q.append((nx,ny))

print(len(answer), *sorted(answer))