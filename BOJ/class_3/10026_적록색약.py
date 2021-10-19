from collections import deque

N = int(input())
graph = [[c for c in input()] for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited_a = [[0]*N for _ in range(N)]
visited_b = [[0]*N for _ in range(N)]

cnt_a,cnt_b = 0,0
for i in range(N):
    for j in range(N):
        if not visited_a[i][j]:
            visited_a[i][j] = 1
            queue = deque()
            queue.append((i,j))
            while queue:
                x,y = queue.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if (0 <= nx < N) and (0 <= ny < N) and (graph[nx][ny] == graph[i][j]) and (not visited_a[nx][ny]):
                        queue.append((nx,ny))
                        visited_a[nx][ny] = 1
            cnt_a += 1
        
        if not visited_b[i][j]:
            visited_b[i][j] = 1
            queue = deque()
            queue.append((i,j))
            while queue:
                x,y = queue.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if (0 <= nx < N) and (0 <= ny < N) and (not visited_b[nx][ny]):
                        if graph[i][j] == "B":
                            if graph[nx][ny] == "B":
                                queue.append((nx,ny))
                                visited_b[nx][ny] = 1
                        else:
                            if graph[nx][ny] != "B":
                                queue.append((nx,ny))
                                visited_b[nx][ny] = 1
            cnt_b += 1

print(cnt_a, cnt_b)