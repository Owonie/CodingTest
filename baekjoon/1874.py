# 시간제한 2초
import sys
input = sys.stdin.readline

n = int(input())
s = []
ans = []
cnt = 1

for _ in range(n):
    temp = int(input())
    while cnt <= temp:
        s.append(cnt)
        ans.append('+')
        cnt += 1
    if s[-1] == temp:
        s.pop()
        ans.append('-')
    else:
        ans = ['NO']
        break
for i in ans:
    print(i)
