# 시간제한 0.5초
import sys
from collections import deque
input = sys.stdin.readline

q = deque()

n = int(input())

for _ in range(n):
    temp = []
    temp = input().split()
    temp.append('0')
    if temp[0] == 'push':
        q.append(temp[1])
    elif temp[0] == 'pop':
        if len(q)>0:
            print(q.popleft())
        else:
            print(-1)
    elif temp[0] == 'size':
        print(len(q))
    elif temp[0] == 'empty':
        if len(q) > 0:
            print(0)
        else:
            print(1)
    elif temp[0] == 'front':
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)
    elif temp[0] == 'back':
        if len(q) >0 :
            print(q[-1])
        else:
            print(-1)
