# 시간제한 2초

import sys
input =sys.stdin.readline
from collections import deque

n,k = map(int,input().split())
arr = list(map(str,input().split()))
visited = set("".join(arr))

last = sorted(arr)

ans = -1

q = deque([[arr,0]])

while q:
    arr, cnt = q.popleft()
    if arr == last:
        ans = cnt
        break
    for i in range(n-k+1):
        temp = arr[i:i+k]
        temp.reverse()
        arr2 = arr[:i] + temp + arr[i+k:]
        str2 = "".join(arr2)
        if str2 not in visited:
            q.append([arr2,cnt+1])
            visited.add(str2)
print(ans)
