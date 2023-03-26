# 시간제한 1.5초

import sys
input = sys.stdin.readline
m = int(input())
s = set()
for _ in range(m):
    temp = list(map(str,input().split()))
    if temp[0] == 'add':
        s.add(int(temp[1]))
    elif temp[0] == 'remove':
            s.discard(int(temp[1]))
    elif temp[0] == 'check':
        if int(temp[1]) in s:
            print(1)
        else:
            print(0)
    elif temp[0] == 'toggle':
        if int(temp[1]) in s:
            s.discard(int(temp[1]))
        else:
            s.add(int(temp[1]))
    elif temp[0] == 'all':
        s = set([i for i in range(1,21)])
    elif temp[0] == 'empty':
        s = set()
