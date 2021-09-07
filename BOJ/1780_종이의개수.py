import sys

def dfs(x,y,n):
    global a,b,c
    topleft = paper[x][y]
    stop = False
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != topleft:
                m = n // 3
                dfs(x, y, m)
                dfs(x+m, y, m)
                dfs(x+2*m, y, m)
                dfs(x, y+m, m)
                dfs(x+m, y+m, m)
                dfs(x+2*m, y+m, m)
                dfs(x, y+2*m, m)
                dfs(x+m, y+2*m, m)
                dfs(x+2*m, y+2*m, m) 
                stop = True
                break
        if stop == True:
            break
    
    if stop == False:
        if topleft == -1:
            a += 1
        elif topleft == 0:
            b += 1
        else:
            c += 1

N = int(sys.stdin.readline().rstrip())
paper = []
for _ in range(N):
    paper.append(list(map(int, sys.stdin.readline().rstrip().split())))

a,b,c = 0,0,0
dfs(0, 0, N)
print(a)
print(b)
print(c)