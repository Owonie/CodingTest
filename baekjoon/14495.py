# 시간제한 2초

n = int(input())

dp = [1,1,1,2]

for i in range(4,n+1):
    dp.append(dp[i-1] + dp[i-3]
print(dp[n-1])
