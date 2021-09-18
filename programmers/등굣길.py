def solution(m, n, puddles):
    from collections import deque
    
    graph = [[0]*m for _ in range(n)]
    dp = [[1]*m for _ in range(n)]
    for puddle in puddles:
        y,x = puddle
        graph[x-1][y-1] = 1
        dp[x-1][y-1] = 0
        if x-1 == 0:
            for j in range(y-1,m):
                dp[0][j] = 0
        elif y-1 == 0:
            for i in range(x-1,n):
                dp[i][0] = 0
    
    for i in range(1,n):
        for j in range(1,m):
            if graph[i][j] != 1:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    answer = dp[n-1][m-1]%1000000007
    return answer