import sys
from collections import deque

M,N = map(int, sys.stdin.readline().rstrip().split())
tomato = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append((i,j))

if len(queue) == M*N:
    print(0)
    exit()

day = 0
while queue:
    for _ in range(len(queue)):
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if tomato[nx][ny] == 0:
                    tomato[nx][ny] = 1
                    queue.append((nx,ny))
    day += 1

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            print(-1)
            exit()
print(day-1)