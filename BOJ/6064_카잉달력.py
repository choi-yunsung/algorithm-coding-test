import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().rstrip().split())
    next = False
    for i in range(N): # x를 기준으로 y 체크
        if (i*M + x)%N == y:
            print(i*M + x)
            break
    else:
        next = True
    
    if next: # x를 기준으로 실패시 y 기준으로 x 체크
        for j in range(M):
            if (j*N + y)%M == x:
                print(j*N + y)
                break
        else:
            print(-1)