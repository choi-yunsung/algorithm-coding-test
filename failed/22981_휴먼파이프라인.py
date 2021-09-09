import math

N,K = map(int, input().split())
velocity = sorted(list(map(int, input().split())))

min_v = velocity[0]
best = 0
for i in range(1, len(velocity)):
    temp = min_v*i + velocity[i]*(len(velocity)-i)
    best = max(best, temp)

answer = math.ceil(K/best)
print(answer)