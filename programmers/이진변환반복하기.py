def solution(s):
    answer = [0,0]
    while s != '1':
        ones = 0
        for i in s:
            if i == '1':
                ones += 1
            else:
                answer[1] += 1
        s = bin(ones)[2:]
        answer[0] += 1
    
    return answer