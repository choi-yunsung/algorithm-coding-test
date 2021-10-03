from collections import deque

# def num_to_str(num):
#     return (4-len(str(num)))*'0' + str(num)

for _ in range(int(input())):
    visited = set()

    a,b = map(int, input().split())
    # b = num_to_str(b)

    q = deque([(a,'')])
    visited.add(a)
    while True:
        now, text = q.popleft()
        # now = num_to_str(now)

        if now == b:
            print(text)
            break

        d = (now*2)%100
        s = now-1 if now>0 else 9999
        l = (now % 1000)*10 + now//1000
        r = (now % 10)*1000 + now//10
        
        if d not in visited:
            q.append((d, text+'D'))
            visited.add(d)
        if s not in visited:
            q.append((s, text+'S'))
            visited.add(s)
        if l not in visited:
            q.append((l, text+'L'))
            visited.add(l)
        if r not in visited:
            q.append((r, text+'D'))
            visited.add(r)
