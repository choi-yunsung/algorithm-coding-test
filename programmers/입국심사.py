def solution(n, times):
    start = 1
    end = max(times)*n
    answer = 0
    
    while start <= end:
        mid = (start+end)//2
        cnt = 0
        for i in times:
            cnt += mid//i

        if cnt >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer