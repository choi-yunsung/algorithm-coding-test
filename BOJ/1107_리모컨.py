N = int(input())
M = int(input())
remote = set([str(i) for i in range(10)])
if M:
    remote -= set(map(str, input().split()))

now = 100
cnt = abs(now - N)
for channel in range(1000001):
    for i in range(len(str(channel))):
        if str(channel)[i] not in remote:
            break
    else:
        cnt = min(cnt, len(str(channel)) + abs(channel - N))

print(cnt)