import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().rstrip().split())
    a,b = 0,0
    for i in range(1, M*N+1):
        if a < M:
            a += 1
        else:
            a = 1

        if b < N:
            b += 1
        else:
            b = 1
        
        if a == x and b == y:
            print(i)
            break
    else:
        print(-1)