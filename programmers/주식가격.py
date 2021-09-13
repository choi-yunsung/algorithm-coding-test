def solution(prices):
    answer = [0]*len(prices)
    idx = []
    for i, price in enumerate(prices):
        while idx and price < prices[idx[-1]]:
            j = idx.pop()
            answer[j] = i-j
        idx.append(i)
        
    while idx:
        j = idx.pop()
        answer[j] = len(prices) - j - 1
    
    return answer