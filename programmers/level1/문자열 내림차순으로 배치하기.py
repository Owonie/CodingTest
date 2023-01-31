def solution(s):
    answer = list(map(str,s))
    answer.sort(reverse = True)
    answer = "".join(answer)
    return answer
