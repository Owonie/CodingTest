# 시간제한 1초

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [1,-1,0,0,1,1,-1,-1]
dy = [0,0,1,-1,1,-1,1,-1]
def dfs(x,y):
    graph[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
            dfs(nx,ny)
while(True):
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    graph = []
    for i in range(h):
        temp = list(map(int,input().split()))
        graph.append(temp)
    cnt = 0
    for j in range(h):
        for k in range(w):
            if graph[j][k] == 1:
                dfs(j,k)
                cnt += 1
    print(cnt)
