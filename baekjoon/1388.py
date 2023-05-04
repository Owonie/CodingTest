# 시간제한 2초

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
dx = [-1,1]
dy = [-1,1]
def dfs(x,y):
    if graph[x][y] == "-":
        graph[x][y] = "0"
        for k in dy:
            ny = y + k
            if 0 < ny < m and graph[x][ny] == "-":
                dfs(x,ny)

    if graph[x][y] == "|":
        graph[x][y] = "0"
        for l in dx:
            nx = x + l
            if 0 < nx < n and graph[nx][y] == "|":
                dfs(nx,y)

graph = []
cnt = 0
for _ in range(n):
    temp = list(input())
    graph.append(temp)
for i in range(n):
    for j in range(m):
        if graph[i][j] == "-" or graph[i][j] == "|":
            dfs(i,j)
            cnt += 1

print(cnt)
