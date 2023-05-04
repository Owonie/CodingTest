# 시간제한 1초

import sys
input = sys.stdin.readline

def dfs(idx,cnt):
    visited[idx] = True
    for i in graph[idx]:
        if visited[i] == False:
            cnt = dfs(i,cnt+1)
    return cnt

n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]
visited = [False] *(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = dfs(1,0)
print(cnt)
