# 시간제한 1초

import sys
input = sys.stdin.readline
n,m,b = map(int,input().split())
ground = [list(map(int,input().split())) for _ in range(n)]
ans = 100000000
floor = 0
for i in range(257):
    plus = 0
    minus = 0
    for j in range(n):
        for k in range(m):
            if ground[j][k] >= i:
                plus += ground[j][k] - i
            else:
                minus += i - ground[j][k]
    if plus >= minus - b:
        if ans >= minus + 2*plus:
            ans = minus + 2*plus
            floor = i
print(ans,floor)
