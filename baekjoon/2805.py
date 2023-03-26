# 시간제한 1초

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))


min_length = 1
max_length = sum(arr)
while(min_length <= max_length):
    cnt = 0
    temp = (min_length+max_length)//2
    for i in arr:
        if i - temp > 0:
            cnt += i-temp
    if cnt >= m:
        min_length = temp + 1
    elif cnt < m:
        max_length = temp - 1
    
print(max_length)
