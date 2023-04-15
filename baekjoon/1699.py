# 시간제한 2초

n = int(input())

dp = [0] * (n+1)
arr = []
for _ in range(1,320):
    arr.append(_*_)
for i in range(1,n+1):
    ans = []
    for j in arr:
        if j > i:
            break
        ans.append(dp[i-j])
    dp[i] = min(ans)+1
print(dp[n])
