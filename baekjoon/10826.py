# 시간제한 1초

dp = [0,1]

n = int(input())
if n >= 2:        
    for i in range(2,n+1):
        dp.append(dp[i-1]+dp[i-2])
    print(dp[-1])
else:
    print(n)
