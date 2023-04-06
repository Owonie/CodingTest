# 시간제한 2초

n = int(input())
dp = [4,6]

for i in range(2,n+1):
    dp.append(dp[i-1]+dp[i-2])
print(dp[n-1])
