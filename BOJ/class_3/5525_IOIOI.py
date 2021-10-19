N = int(input())
M = int(input())
S = input()

answer = 0
cnt = 0
for i in range(1, M-1):
    if S[i-1] == 'I' and S[i] == 'O' and S[i+1] == 'I':
        cnt += 1
        if cnt == N:
            answer += 1
            cnt -= 1
    elif S[i-1] == 'O' and S[i] == 'I' and S[i+1] == 'O':
        continue
    else:
        cnt = 0
print(answer)