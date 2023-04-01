# 시간제한 0.5초
import math
n = int(input())
dp = [0,1]
for i in range(2,n+1):
    cnt =4
    for j in range(int(math.sqrt(i)),0,-1):
        cnt = min(cnt,dp[i-j**2]+1)
    dp.append(cnt)
print(dp[n])
