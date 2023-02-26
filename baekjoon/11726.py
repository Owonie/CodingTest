# 시간 제한 1초

n = int(input())
dp = [0] * (n+1)

def dynamic(num):
    if num == 1:
        return 1
    if num == 2:
        return 2
    if dp[num] != 0:
        return dp[num]
    dp[num] = (dynamic(num-1)+dynamic(num-2))%10007
    return dp[num]
print(dynamic(n))

