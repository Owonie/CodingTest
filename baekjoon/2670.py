# 시간제한 1초

import sys
input = sys.stdin.readline

n = int(input())
ans = 1
max_ans = 0
for i in range(n):
    temp = float(input())
    ans = max(temp,temp*ans)
    if ans > max_ans:
        max_ans = ans
print('%0.3f'% max_ans)
