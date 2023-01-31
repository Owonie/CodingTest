def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    for i in new_id:
        if i.isalnum() or i in '-_.':
            answer += i
    while '..' in answer:
        answer = answer.replace('..','.')
    answer = answer.strip('.')
    if answer == '':
        answer ='a'
    if len(answer)>15:
        answer = answer[:15]
        answer = answer.strip('.')
    if len(answer)<3:
        answer = answer + answer[-1] * (3-len(answer))
    return answer
