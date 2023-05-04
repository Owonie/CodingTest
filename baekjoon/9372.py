# 시간제한 1초

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
t = int(input())

def dfs(idx,cnt):
    visited[idx] = True
    for country in route[idx]:
        if visited[country] == False:
            cnt = dfs(country,cnt+1)    
    return cnt

for i in range(t):
    n,m = map(int,input().split())
    visited = [False]*(n+1)
    route = [[] for _ in range(n+1)]
    for j in range(m):
        a,b = map(int,input().split())
        route[a].append(b)
        route[b].append(a)
    cnt  = dfs(1,0)
    print(cnt)
