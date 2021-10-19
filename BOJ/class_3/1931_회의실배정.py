import sys

N = int(sys.stdin.readline().rstrip())
meetings = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
meetings.sort(key=lambda x: (x[1], x[0]))

end = 0
answer = 0
for m in meetings:
    if end <= m[0]:
        end = m[1]
        answer += 1

print(answer)