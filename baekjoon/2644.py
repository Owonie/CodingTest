# 시간제한 1초

import sys
input = sys.stdin.readline

n = int(input())
start,end = map(int,input().split())
m = int(input())
graph = [[] for i in range(n+1)]
visited = [0]*(n+1)
ans = -1
def dfs(idx,depth):
    global ans
    visited[idx] = 1
    if idx == end:
        ans = depth
        return
    for i in graph[idx]:
        if visited[i] == 0:
            dfs(i,depth+1)

for _ in range(1,m+1):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(start,0)
print(ans)
