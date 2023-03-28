# 시간제한 1초

n= int(input())

dp = [0,1,3]
for _ in range(3,n+1):
    dp.append((dp[i-1])+(2*(dp[i-2])))
print(dp[n] % 10007)
