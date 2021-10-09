def solution(grid):
    def get_next(row,col,direction):
        """다음 격자와 다음 방향을 return 하는 함수"""
        if direction == 0:  # up
            if grid[row][col] == 'S':
                nx,ny,nd = row-1,col,direction
                if nx < 0:
                    nx = n_row - 1
            elif grid[row][col] == 'L':
                nx,ny,nd = row,col-1,2
                if ny < 0:
                    ny = n_col - 1
            elif grid[row][col] == 'R':
                nx,ny,nd = row,col+1,3
                if ny == n_col:
                    ny = 0
                    
        elif direction == 1:  # down
            if grid[row][col] == 'S':
                nx,ny,nd = row+1,col,direction
                if nx == n_row:
                    nx = 0
            elif grid[row][col] == 'L':
                nx,ny,nd = row,col+1,3
                if ny == n_col:
                    ny = 0
            elif grid[row][col] == 'R':
                nx,ny,nd = row,col-1,2
                if ny < 0:
                    ny = n_col - 1
                    
        elif direction == 2:  # left
            if grid[row][col] == 'S':
                nx,ny,nd = row,col-1,direction
                if ny < 0:
                    ny = n_col - 1
            elif grid[row][col] == 'L':
                nx,ny,nd = row+1,col,1
                if nx == n_row:
                    nx = 0
            elif grid[row][col] == 'R':
                nx,ny,nd = row-1,col,0
                if nx < 0:
                    nx = n_row - 1
                    
        elif direction == 3:  # right
            if grid[row][col] == 'S':
                nx,ny,nd = row,col+1,direction
                if ny == n_col:
                    ny = 0
            elif grid[row][col] == 'L':
                nx,ny,nd = row-1,col,0
                if nx < 0:
                    nx = n_row - 1
            elif grid[row][col] == 'R':
                nx,ny,nd = row+1,col,1
                if nx == n_row:
                    nx = 0
        return nx,ny,nd
            
            
    answer = []

    n_col = len(grid[0])
    n_row = len(grid)
    
    array = [] # 지나간 경로 여부를 확인하는 array
    for _ in range(n_row):
        array.append([[0,0,0,0] for _ in range(n_col)])
    
    for i in range(n_row):
        for j in range(n_col):
            for k in range(4):  # direction = [up, down, left, right]
                # 만약 해당 격자의 해당 방향 경로로 지나가지 않았다면 새로운 경로 시작
                if array[i][j][k] == 0:
                    length = 1
                    array[i][j][k] = 1
                    nx,ny,nk = get_next(i,j,k)
                    while array[nx][ny][nk] != 1:
                        array[nx][ny][nk] = 1
                        length += 1
                        nx, ny, nk = get_next(nx,ny,nk)
                    answer.append(length)
                        
    return sorted(answer)