import sys
from collections import deque

M,N,H = map(int, sys.stdin.readline().rstrip().split())
tomato = []
for _ in range(H):
    layer = []
    for _ in range(N):
        layer.append(list(map(int, sys.stdin.readline().rstrip().split())))
    tomato.append(layer)

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

queue = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 1:
                queue.append((i,j,k))

if len(queue) == M*N*H:
    print(0)
    exit()

day = 0
while queue:
    for _ in range(len(queue)):
        z,x,y = queue.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if nz >= 0 and nz < H and nx >= 0 and nx < N and ny >= 0 and ny < M:
                if tomato[nz][nx][ny] == 0:
                    tomato[nz][nx][ny] = 1
                    queue.append((nz,nx,ny))
    day += 1

for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 0:
                print(-1)
                exit()
print(day-1)