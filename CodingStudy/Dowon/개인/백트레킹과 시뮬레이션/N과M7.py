# 시간제한 1초
import sys
input = sys.stdin.readline
from itertools import product
n,m = map(int,input().split())

arr = list(map(int,input().split()))
ans = []
for nums in product(arr,repeat=m):
    temp = list(nums)

    ans.append(temp)

ans.sort()
for i in ans:
    print(*i)
