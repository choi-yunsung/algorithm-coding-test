def dfs(i, j, topleft, l):
    global r,c
    if l == 2:
        r = r%2
        c = c%2
        if r == 0 and c == 0:
            print(topleft)
        if r == 0 and c == 1:
            print(topleft+1)
        if r == 1 and c == 0:
            print(topleft+2)
        if r == 1 and c == 1:
            print(topleft+3)
        return        
    else:
        l = l//2
        if r < i+l and c < j+l:
            dfs(i, j, topleft, l)
        if r < i+l and c >= j+l:
            dfs(i, j+l, topleft+l**2, l)
        if r >= i+l and c < j+l:
            dfs(i+l, j, topleft+l**2*2 ,l)
        if r >= i+l and c >= j+l:
            dfs(i+l, j+l, topleft+l**2*3, l)

n,r,c = map(int, input().split())
dfs(0, 0, 0, 2**n)