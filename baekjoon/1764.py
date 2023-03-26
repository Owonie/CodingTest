# 시간제한 2초
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
a = set()
b = set()
for i in range(n):
    a.add(input().strip())
for j in range(m):
    b.add(input().strip())
ans = list(a&b)
ans.sort()
print(len(ans))
print(*ans,sep='\n')
