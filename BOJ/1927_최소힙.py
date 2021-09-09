import heapq
import sys

N = int(sys.stdin.readline().rstrip())
numbers = []
for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if numbers:
            print(heapq.heappop(numbers))
        else:
            print(0)
    else:
        heapq.heappush(numbers, x)