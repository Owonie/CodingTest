# 시간제한 1초

import sys
input = sys.stdin.readline
dp = [0] * 1000002
dp[0] = 1
dp[1]= 2
dp[2] = 4
for _ in range(3,1000000):
    dp[_] = (dp[_-1]+dp[_-2]+dp[_-3])%1000000009
t = int(input())
for i in range(t):
    temp = int(input())
    print(dp[temp-1])
