import sys
from itertools import combinations

n,m = map(int, sys.stdin.readline().split())

graph = []
house =[]
chicken = []
for i in range(n):
    row = []
    for j, x in enumerate(sys.stdin.readline().split()):
        if int(x) == 1:
            house.append((i,j))
        elif int(x) == 2:
            chicken.append((i,j))
        row.append(int(x))
    graph.append(row)

answer = int(1e9)
for cmb in list(combinations(chicken, m)):
    city_distance = 0
    for hx, hy in house:
        house_distance = int(1e9)
        for cx, cy in cmb:
            dist = abs(hx-cx) + abs(hy-cy)
            house_distance = min(house_distance, dist)
        city_distance += house_distance
    answer = min(answer, city_distance)

print(answer)