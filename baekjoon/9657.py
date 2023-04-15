# 시간제한 1초

n = int(input())
# 상근 -> 0 창영 -> 1
dp = [0,1,0,0]

for i in range(4,n+1):
    if dp[i-1] == 0 and dp[i-3] == 0 and dp[i-4] == 0:
        dp.append(1)
    else:
        dp.append(0)
if dp[n-1] == 1:
    print('CY')
else:
    print('SK')
