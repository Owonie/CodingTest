def solution(n,s):
    answer = []
    temp = -1
    if n > s:
        return [-1]
    if s % n == 0:
        for i in range(n):
            answer.append(int(s/n))
    if s % n != 0:
        count = s % n
        for i in range(n):
            answer.append(int(s//n))
        while count > 0:
            answer[temp] += 1
            temp -= 1
            count -= 1
    return answer
