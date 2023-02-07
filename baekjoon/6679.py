# 시간제한 1초
# 루프로 세가지 진수의 합을 구하고 출력하자

def solution(a,b):
    num = 0
    while a > 0:
        num += a%b
        a = a//b
    return num
for _ in range(1000,10000):
    a = solution(_,10)
    b = solution(_,12)
    c = solution(_,16)
    if a == b and b == c:
        print(_)
