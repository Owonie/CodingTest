# 시간제한 1초

import sys
input = sys.stdin.readline
from itertools import permutations

n,m = map(int,input().split())
arr = list(map(int,input().split()))
ans = []
for num in permutations(arr,m):
    temp = list(num)
    ans.append(temp)
ans.sort()
for i in ans:
    print(*i)
