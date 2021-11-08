def solution(word):
    vowels = {"A": 0, "E": 1, "I": 2, "O": 3, "U": 4}
    patterns = [781, 156, 31, 6, 1]

    answer = 0
    for i in range(len(word)):
        answer += (vowels[word[i]] * patterns[i]) + 1
    return answer
