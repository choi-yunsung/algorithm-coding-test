from collections import deque


def bfs(start, visited, graph):
    queue = deque([start])
    result = 1
    visited[start] = 1
    while queue:
        now = queue.popleft()

        for i in graph[now]:
            if not visited[i]:
                result += 1
                queue.append(i)
                visited[i] = 1
    return result


def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n + 1)]

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    for a, b in wires:
        visited = [0 for _ in range(n + 1)]
        visited[b] = 1
        result = bfs(a, visited, graph)
        answer = min(abs(result - (n - result)), answer)

    return answer
