# 시간제한 2초

import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr = []
for i in range(n):
    a,b = map(int,input().split())
    arr.append((a,b))
print(arr)
