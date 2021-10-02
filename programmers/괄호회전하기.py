def solution(s):
    answer = 0
    
    pair = {
        ']':'[',
        '}':'{',
        ')':'('
    }
    
    for i in range(len(s)):
        new_s = s[i:] + s[:i]
        
        temp = []
        for bracket in new_s:
            if bracket in "[({":
                temp.append(bracket)
            elif temp != [] and pair[bracket] == temp[-1]:
                temp.pop()
            else:
                break
        else:
            if temp == []:
                answer += 1

    return answer