from itertools import cycle

def solution(answers):
    answer = []
    cycle1 =cycle([1,2,3,4,5])
    cycle2 = cycle([2,1,2,3,2,4,2,5])
    cycle3 = cycle([3,3,1,1,2,2,4,4,5,5])
    result = {'1':0,'2':0,'3':0}
    maxi = 0
    for i in answers:
        num1 = next(cycle1)
        num2 = next(cycle2)
        num3 = next(cycle3)
        if i == num1: result['1'] +=1
        if i == num2: result['2'] +=1
        if i == num3: result['3'] +=1
    maxi = max(result.values())
    for i in result:
        if result[i] == maxi:
            answer.append(int(i))
    return answer
