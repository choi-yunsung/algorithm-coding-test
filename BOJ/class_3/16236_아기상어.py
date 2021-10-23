from collections import deque

n = int(input())
fish = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if fish[i][j] == 9:
            shark_x, shark_y = i, j
            fish[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(start_x, start_y, size):
    q = deque()
    q.append((start_x, start_y, 0))
    visited = [[0] * n for _ in range(n)]
    victim = []
    while q:
        now_x, now_y, dist = q.popleft()
        if visited[now_x][now_y]:
            continue
        visited[now_x][now_y] = dist
        if fish[now_x][now_y] < size and fish[now_x][now_y] != 0:
            victim.append((dist, now_x, now_y))
        for i in range(4):
            next_x = now_x + dx[i]
            next_y = now_y + dy[i]
            if (
                (0 <= next_x < n)
                and (0 <= next_y < n)
                and (fish[next_x][next_y] <= size)
            ):
                q.append((next_x, next_y, dist + 1))
    if not victim:
        return (-1, -1, -1)
    victim.sort()
    fish[victim[0][1]][victim[0][2]] = 0
    return victim[0]


answer = 0
shark_size = 2
continue_flag = True
while continue_flag:
    for _ in range(shark_size):
        time, x, y = bfs(shark_x, shark_y, shark_size)
        if time == -1:
            continue_flag = False
            break
        shark_x, shark_y = x, y
        answer += time
    else:
        shark_size += 1

print(answer)
