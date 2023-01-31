def solution(n):
    answer = getMyDivisor(n)
    
    return answer

def getMyDivisor(n):
    divisorsList = []
    for i in range(1, n + 1):
        if (n % i == 0) :
            divisorsList.append(i)
    return sum(divisorsList)
