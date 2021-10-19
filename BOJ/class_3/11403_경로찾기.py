import sys

N = int(sys.stdin.readline().rstrip())
graph = [list(map(str, sys.stdin.readline().rstrip().split())) for _ in range(N)]

for k in range(N):
    for a in range(N):
        for b in range(N):
            if graph[a][b] == '1':
                continue
            else:
                if graph[a][k] == '1' and graph[k][b] == '1':
                    graph[a][b] = '1'
                
for i in range(N):
    print(' '.join(graph[i]))