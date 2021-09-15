from collections import deque

N,K = map(int, input().split())

if N == K:
    print(0)
    exit(0)

q = deque([(N,0)])
visited = [0] * 100001
while q:
    now, sec = q.popleft()
    for next in [now*2, now+1, now-1]:
        if next == K:
            print(sec+1)
            q.clear()
            break
        if next >= 0 and next <= 100000 and not visited[next]:
            visited[next] = True
            q.append((next, sec+1))