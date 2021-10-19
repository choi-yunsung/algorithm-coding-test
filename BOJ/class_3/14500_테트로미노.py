n,m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

def tetromino_bar(x,y):
    if x+4 <= n:
        v = sum([paper[i][y] for i in range(x,x+4)])
    else:
        v = 0

    if y+4 <= m:
        h = sum([paper[x][j] for j in range(y,y+4)])
    else:
        h = 0
    return max(v,h)

def tetromino_square(x,y):
    if x+2 <= n and y+2 <= m:
        return sum([paper[i][j] for i in range(x,x+2) for j in range(y,y+2)])
    return 0

def tetromino_etc(x,y):
    if x+3 <= n and y+2 <= m:
        base = sum([paper[i][j] for i in range(x,x+3) for j in range(y,y+2)])
        deleted = min(
            paper[x][y]+paper[x+1][y],
            paper[x+1][y]+paper[x+2][y],
            paper[x][y+1]+paper[x+1][y+1],
            paper[x+1][y+1]+paper[x+2][y+1], # 주황색
            paper[x][y+1]+paper[x+2][y],
            paper[x][y]+paper[x+2][y+1], # 초록색
            paper[x][y]+paper[x+2][y],
            paper[x][y+1]+paper[x+2][y+1] # 보라색
        )
        v = base-deleted
    else:
        v = 0

    if x+2 <= n and y+3 <= m:
        base = sum([paper[i][j] for i in range(x,x+2) for j in range(y,y+3)])
        deleted = min(
            paper[x][y]+paper[x][y+1],
            paper[x][y+1]+paper[x][y+2],
            paper[x+1][y]+paper[x+1][y+1],
            paper[x+1][y+1]+paper[x+1][y+2], # 주황색
            paper[x][y]+paper[x+1][y+2],
            paper[x+1][y]+paper[x][y+2], # 초록색
            paper[x][y]+paper[x][y+2],
            paper[x+1][y]+paper[x+1][y+2] # 보라색
        )
        h = base-deleted
    else:
        h = 0
    return max(v,h)


answer = 0
for i in range(n):
    for j in range(m):
        answer = max(answer, tetromino_bar(i,j), tetromino_square(i,j), tetromino_etc(i,j))

print(answer)