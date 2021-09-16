import sys
N = int(sys.stdin.readline().rstrip())
graph = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

def dfs(row, col, size):
    next = False
    for i in range(row, row+size):
        for j in range(col, col+size):
            if graph[row][col] != graph[i][j]:
                next = True
                break
        if next:
            break
    
    if not next:
        return str(graph[row][col])
    else:
        size = size//2
        return '(' + dfs(row, col, size) + dfs(row, col+size, size)\
            + dfs(row+size, col, size) + dfs(row+size, col+size, size) + ')'

print(dfs(0,0,N))