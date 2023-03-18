# 시간제한 0.5초

import sys
from collections import deque
q = deque()
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    order = list(map(str,input().split()))
    if order[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif order[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'push_front':
        q.appendleft(order[1])
    elif order[0] == 'push_back':
        q.append(order[1])
    elif order[0] == 'pop_front':
        if len(q) != 0:
            print(q.popleft())
        else:
            print(-1)
    elif order[0] == 'pop_back':
        if len(q) != 0:
            print(q.pop())
        else:
            print(-1)
