# 시간제한 1초

import sys
input = sys.stdin.readline

t = int(input())

for case in range(t):
    n = int(input())
    arr = {}
    for _ in range(n):
        a,b = map(str,input().split())
        if b in arr:
            arr[b] +=1
        else:
            arr[b] = 1
    temp = 1
    for key, value in arr.items():
        temp *= value+1
    print(temp-1)
    
