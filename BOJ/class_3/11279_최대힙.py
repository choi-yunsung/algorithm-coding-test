import heapq
import sys

N = int(sys.stdin.readline().rstrip())
nums = []
for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if nums:
            print(-heapq.heappop(nums))
        else:
            print(0)
    else:
        heapq.heappush(nums, -x)