# 시간제한 2초

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr2 = sorted(list(set(arr)))

ans = {}

for i in range(len(arr2)):
    ans[arr2[i]] = i

for i in arr:
    print(ans[i], end=' ')
