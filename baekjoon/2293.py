# 시간제한 0.5초

n,k = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

dp = [0] * (k +1)

dp[0] = 1

for i in arr:
    for _ in range(i,k+1):
        temp = dp[_-i]
        dp[_] += temp
print(dp[k])
