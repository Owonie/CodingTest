# 시간제한 1초
# 선 앞뒤 정렬 / 후 상하 정렬

import sys
input = sys.stdin.readline

from itertools import combinations

n,m = map(int,input().split())

arr = list(map(int,input().split()))
ans  =[]
for nums in combinations(arr,m):
    temp = list(nums)
    temp.sort()
    ans.append(temp)
ans.sort()
for i in ans:
    print(*i)
