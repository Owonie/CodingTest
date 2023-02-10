# 시간제한 2초

# 탈출 조건 : 누적 합이 >= N+1 일때

# 시작점이 1일일때........ n일일때
import sys

input = sys.stdin.readline
n = int(input())
T = []
P = []
ans = 0
max_ans = 0
d = [0] * (n+1)
for i in range(n):
    t,p = map(int,input().split())
    T.append(t)
    P.append(p)
for i in range( n -1 , -1, -1):
    if i + T[i] >n:
        d[i] = d[i+1]
    else:
        d[i] = max(d[i+1],P[i] + d[i+T[i]])
print(d[0])
