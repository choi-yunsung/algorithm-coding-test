N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

answer = 0
for coin in coins[::-1]:
    if coin<=K:
        answer += K//coin
        K = K%coin
    if K == 0:
        break
print(answer)