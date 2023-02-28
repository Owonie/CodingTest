# 시간제한 0.5초
from collections import Counter
n,k = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

dp = [0] * (k +1)
print(dp)
