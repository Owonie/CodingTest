#  시간 제한 0.5초
n = int(input())

dp = [i for i in range(n+1)]
arr = [i for i in range(n+1)]
dp[1]= 0
arr[1] = 0
# 1은 실행하지 않는다.

for i in range(2, n+1):
    #dp 배열을 모두 채울 때 까지 실행하기
    dp[i] = dp[i-1]+1
    arr[i] = i-1
    #횟 수 1 증가 ( cnt ~= dp )
    if i % 3 == 0 and dp[i] > dp[i//3]+1:
        dp[i] = dp[i//3] + 1
        arr[i] = i//3
    if i % 2 == 0 and dp[i] > dp[i//2]+1:
        dp[i] = dp[i//2] +1
        arr[i] = i//2

print(dp[n])
print(n, end=" ")
_ = n
while arr[_] != 0:
    print(arr[_], end=" ")
    _ = arr[_]
