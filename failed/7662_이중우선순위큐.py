import heapq

for _ in range(int(input())):
    k = int(input())
    max_q = []
    min_q = []
    for _ in range(k):
        operation, n = input().split()
        if operation == 'I':
            heapq.heappush(min_q, int(n))
            heapq.heappush(max_q, -int(n))
        else:
            if max_q:
                if int(n) == -1:
                    heapq.heappop(min_q)
                    max_q.pop(-1)
                else:
                    heapq.heappop(max_q)
                    min_q.pop(-1)
    
    if min_q:
        print(min_q[-1], min_q[0])
    else:
        print("EMPTY")