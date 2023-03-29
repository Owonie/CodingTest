# 시간제한 0.25초
import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    zero = [1,0]
    one = [0,1]
    n = int(input())
    if n > 1:
        for j in range(n-1):
            zero.append(one[-1])
            one.append(zero[-2]+one[-1])
    print(zero[n],one[n])
