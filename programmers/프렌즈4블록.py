def check(row,col,board):
    topleft = board[row][col]
    if topleft == 0:
        return None
    
    if board[row][col+1] == topleft and board[row+1][col] == topleft and board[row+1][col+1] == topleft:
        return (row, col), (row, col+1), (row+1, col), (row+1, col+1)
    else:
        return None

def drop_blocks():
    pass

def solution(m, n, board):
    board = [[block for block in row] for row in board]
    answer = 0
    while True:
        removed_blocks = []
        for i in range(m - 1):
            for j in range(n - 1):
                result = check(i,j, board)
                if result != None:
                    removed_blocks.extend(result)
        
        removed_blocks = set(removed_blocks)
        if len(removed_blocks) == 0:
            break
        
        for block in removed_blocks:
            board[block[0]][block[1]] = 0
            answer += 1
            
        for j in range(n):
            col = []
            for i in range(m):
                if board[i][j] != 0:
                    col.append(board[i][j])
            col = [0 for _ in range(m - len(col))] + col
            for i in range(m):
                board[i][j] = col[i]

    return answer