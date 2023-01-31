import math
def solution(arrayA,arrayB):
    tempA = arrayA[0]
    tempB = arrayB[0]
    
    answer = 0
    for _ in arrayA:
        tempA = math.gcd(tempA,_)
    for _ in arrayB:
        tempB = math.gcd(tempB,_)
    for _ in arrayA:
        if _ % tempB == 0:
            tempB = 0
            break
    for _ in arrayB:
        if _ % tempA == 0:
            tempA = 0
            break
    answer = max(tempA,tempB)
    return answer
