from collections import deque


def solution(game_board, table):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    blanks = []
    for i in range(len(game_board)):
        for j in range(len(game_board)):
            if game_board[i][j] == 0:
                blank = []
                q = deque()
                q.append((i, j))
                game_board[i][j] = 1
                while q:
                    x, y = q.popleft()
                    blank.append((x, y))
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if (
                            0 <= nx < len(game_board)
                            and 0 <= ny < len(game_board)
                            and game_board[nx][ny] == 0
                        ):
                            q.append((nx, ny))
                            game_board[nx][ny] = 1

                length_x = (
                    max(blank, key=lambda x: x[0])[0]
                    - min(blank, key=lambda x: x[0])[0]
                )
                length_y = (
                    max(blank, key=lambda x: x[1])[1]
                    - min(blank, key=lambda x: x[1])[1]
                )

                shape = [[0 for _ in range(length_y + 1)] for _ in range(length_x + 1)]

                min_x = min(blank, key=lambda x: x[0])[0]
                min_y = min(blank, key=lambda x: x[1])[1]
                for x, y in blank:
                    shape[x - min_x][y - min_y] = 1

                blanks.append(shape)

    pieces = []
    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j] == 1:
                piece = []
                q = deque()
                q.append((i, j))
                table[i][j] = 0
                while q:
                    x, y = q.popleft()
                    piece.append((x, y))
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if (
                            0 <= nx < len(table)
                            and 0 <= ny < len(table)
                            and table[nx][ny] == 1
                        ):
                            q.append((nx, ny))
                            table[nx][ny] = 0

                length_x = (
                    max(piece, key=lambda x: x[0])[0]
                    - min(piece, key=lambda x: x[0])[0]
                )
                length_y = (
                    max(piece, key=lambda x: x[1])[1]
                    - min(piece, key=lambda x: x[1])[1]
                )

                shape = [[0 for _ in range(length_y + 1)] for _ in range(length_x + 1)]

                min_x = min(piece, key=lambda x: x[0])[0]
                min_y = min(piece, key=lambda x: x[1])[1]
                for x, y in piece:
                    shape[x - min_x][y - min_y] = 1

                pieces.append(shape)

    def rotated(a):
        n = len(a)
        m = len(a[0])

        result = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                result[j][n - i - 1] = a[i][j]
        return result

    answer = 0
    for piece in pieces:
        for _ in range(4):
            piece = rotated(piece)
            if piece in blanks:
                blanks.pop(blanks.index(piece))
                answer += sum([sum(i) for i in piece])
                break

    return answer
