# 시간제한 0.5

n = int(input())

dp = [0]*31
dp[0] = 1

for i in range(1,31):
    dp[i] = i*dp[i-1]
for _ in range(n):
    n, m = map(int, input().split())
    print(dp[m]//(dp[n]*(dp[m-n])))
