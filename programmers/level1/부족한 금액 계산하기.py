def solution(price, money, count):
    for i in range(count+1):
        money -= price * i
        print(money)
    if money >= 0:
        return 0
    return abs(money)
