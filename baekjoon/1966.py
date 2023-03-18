# 시간제한 2초
import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    cnt = 0
    n,m = map(int,input().split())
    q = deque(list(map(int,input().split())))
    while(len(q)>0):
        q_max = max(q)
        temp = q.popleft()
        m -= 1
        if temp ==q_max:
            cnt += 1
            if m < 0:
                print(cnt)
                break
        else:
            q.append(temp)
            if m < 0:
                m = len(q) -1

