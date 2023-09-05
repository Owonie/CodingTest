# 시간제한 1초
import sys
input = sys.stdin.readline
from itertools import combinations_with_replacement
n,m = map(int,input().split())

arr = list(map(int,input().split()))
ans = []

for nums in combinations_with_replacement(arr,m):
    temp = list(nums)
    temp.sort()
    ans.append(temp)
ans.sort()
for i in ans:
    print(*i)
