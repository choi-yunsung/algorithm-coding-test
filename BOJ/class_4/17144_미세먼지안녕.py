import sys
r,c,t = map(int, sys.stdin.readline().split())

graph = []
purifier = []
for i in range(r):
    row = []
    for j, x in enumerate(sys.stdin.readline().split()):
        if int(x) == -1:
            purifier.append(i)
        row.append(int(x))
    graph.append(row)


def dust_spread():
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    temp_graph = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] != 0 and graph[i][j] != -1:
                temp = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
                        temp_graph[nx][ny] += graph[i][j]//5
                        temp += graph[i][j]//5
                graph[i][j] -= temp

    for i in range(r):
        for j in range(c):
            graph[i][j] += temp_graph[i][j]

def purifier_upper():
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    direction = 0
    before = 0
    x,y = purifier[0], 1
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if x == purifier[0] and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direction += 1
            continue
        graph[x][y], before = before, graph[x][y]
        x,y = nx,ny

def purifier_lower():
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    direction = 0
    before = 0
    x,y = purifier[1], 1
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if x == purifier[1] and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direction += 1
            continue
        graph[x][y], before = before, graph[x][y]
        x,y = nx,ny


for _ in range(t):
    dust_spread()
    purifier_upper()
    purifier_lower()

answer = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] > 0:
            answer += graph[i][j]
print(answer)