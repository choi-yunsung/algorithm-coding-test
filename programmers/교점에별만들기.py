from itertools import combinations


def solution(line):
    stars = []
    for line_1, line_2 in combinations(line, 2):
        A, B, E = line_1
        C, D, F = line_2

        denominater = A * D - B * C
        if denominater == 0:
            continue
        x = (B * F - E * D) / denominater
        y = (E * C - A * F) / denominater

        if not x.is_integer() or not y.is_integer():
            continue
        else:
            x = int(x)
            y = int(y)

        stars.append((x, y))

    min_x = min(stars, key=lambda x: x[0])[0]
    min_y = min(stars, key=lambda x: x[1])[1]
    max_x = max(stars, key=lambda x: x[0])[0]
    max_y = max(stars, key=lambda x: x[1])[1]

    answer = []
    for i in range(max_y, min_y - 1, -1):
        row = ""
        for j in range(min_x, max_x + 1):
            if (j, i) in stars:
                row += "*"
            else:
                row += "."
        answer.append(row)

    return answer
