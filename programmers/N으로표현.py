def solution(N, number):
    dp = [0]
    for i in range(1, 9):
        numbers = set()
        numbers.add(int(str(N)*i))
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i-j]:
                    numbers.add(a * b)
                    numbers.add(a + b)
                    if a > b:
                        numbers.add(a - b)
                    else:
                        numbers.add(b - a)
                    if a > 0:
                        numbers.add(b // a)
                    if b > 0:
                        numbers.add(a // b)
        if number in numbers:
            return i
        dp.append(numbers)
    return -1