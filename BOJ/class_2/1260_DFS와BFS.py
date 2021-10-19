from collections import deque

def dfs(graph, v, visited_dfs):
    visited_dfs[v] = 1
    print(v, end=' ')
    for i in sorted(graph[v]):
        if not visited_dfs[i]:
            dfs(graph, i, visited_dfs)


def bfs(graph, v, visited_bfs):
    q = deque([v])
    visited_bfs[v] = 1
    while q:
        n = q.popleft()
        print(n, end=' ')
        for i in sorted(graph[n]):
            if not visited_bfs[i]:
                q.append(i)
                visited_bfs[i] = 1


N,M,V = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited_dfs = [0] * (N+1)
visited_bfs = [0] * (N+1)

dfs(graph, V, visited_dfs)
print()
bfs(graph, V, visited_bfs)
