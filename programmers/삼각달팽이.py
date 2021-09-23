def solution(n):
    graph = [[0]*i for i in range(1,n+1)]
    dx = [1,0,-1]
    dy = [0,1,-1]
    start,size = 1,n
    row,col,direction = -1,0,0
    while size > 0:
        for i in range(start, start+size):
            row += dx[direction%3]
            col += dy[direction%3]
            graph[row][col] = i
        start = graph[row][col] + 1
        size -= 1
        direction += 1
    
    answer = []
    for row in graph:
        answer += row
    
    return answer