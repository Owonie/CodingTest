# 시간제한 1초

k = int(input())

dp = [0,1]
if k == 0:
    print(0,1)
else:
    for i in range(2,k+1):
        dp.append(dp[i-1]+dp[i-2])
print(dp[k-1],dp[k])
