def solution(phone_number):
    answer = ''
    stra = phone_number[len(phone_number)-4:]
    for i in range(len(phone_number)-4):
        answer += '*'
    answer += stra
    return answer
