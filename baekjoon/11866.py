# 시간제한 2초
from collections import deque
n,k = map(int,input().split())
q = deque()
ans = []
for _ in range(1,n+1):
    q.append(_)
while(len(q)>0):
    for i in range(1,k):
        temp = q.popleft()
        q.append(temp)
    ans.append(q.popleft())
print('<',end='')
print(*ans,sep=', ',end='')
print('>')
