# 시간제한 1초

import sys
input= sys.stdin.readline
dp = [0]*1000000
def dynamic(number):
    if number == 1:
        return 1
    elif number == 2:
        return 2
    elif number == 3:
        return 4
    
    if dp[number] != 0:
        return dp[number]
    else:
        dp[number] = dynamic(number-1)+dynamic(number-2)+dynamic(number-3)
        return dp[number]
n = int(input())
for i in range(n):
    temp = int(input())
    print(dynamic(temp))
    
