# 시간 제한 2초
import sys
input = sys.stdin.readline

one = list(input().strip())
two = list(input().strip())

h,w = len(one),len(two)
dp = [[0]*(w+1) for _ in range(h+1)]

for i in range(1,h+1):
    for j in range(1,w+1):
        if one[i-1] == two[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])
print(dp[-1][-1])
