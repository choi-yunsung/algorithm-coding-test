def solution(numbers):
    answer = []
    for number in numbers:
        # 짝수인 경우 1을 더함
        if number%2 == 0:
            answer.append(number+1)
        # 홀수인 경우 2**(비트의 뒷자리부터 0이 나올때까지의 1의 개수 - 1)를 더함
        else:
            binary = bin(number)[2:]
            for i, s in enumerate(str(binary)[::-1]):
                if s == '0':
                    answer.append(number + 2**(i-1))
                    break
            else: # 비트에 0이 없는 경우 2**(비트의 길이 - 1)를 더함
                answer.append(number + 2**(len(str(binary))-1))
    return answer