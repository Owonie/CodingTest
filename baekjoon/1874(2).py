# 시간제한 2초
from collections import deque

n = int(input())
arr = []
s = []
ans = []
for _ in range(n):
    arr.append(int(input().strip()))
arr.append(0)
for i in range(1,n+1):
    if i == 1:
        s.append(i)
        ans.append('+')
    elif s[-1] == arr[i-1]:
        s.pop()
        ans.append('-')
    elif i == arr[i-1]:
        ans.append('+')
        ans.append('-')
    elif i > arr[i-1]:
        if i != s[-1]:
            ans = ['NO']
            break
    elif i < arr[i-1]:
        s.append(i)
        ans.append('+')
print(*ans,end='\n')
