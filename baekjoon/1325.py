# 시간제한 5초
import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)


def bfs(idx):
    cnt = 1
    visited = [0]*(n+1)
    visited[idx] = 1
    q = deque([idx])
    while q:
        node = q.popleft()
        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = 1
                cnt += 1
                q.append(i)
    return cnt
ans = []
for i in range(1,n+1):
    ans.append(bfs(i))
value = max(ans)
for i in range(n):
    if value == ans[i]:
        print(i+1,end=' ')
