# 시간제한 3초

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n,m = map(int,input().split())

graph = list([] for _ in range(n+1))
cnt = 0

for i in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n+1)
def dfs(x):
    visited[x] = True

    for node in graph[x]:
        if not visited[node]:
            dfs(node)

cnt = 0
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1
    
print(cnt)
