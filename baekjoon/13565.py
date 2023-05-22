# 시간 제한 1초

import sys
from collections import deque
input = sys.stdin.readline

m,n = map(int,input().split())
graph = []

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(j):
    visited = [[0]*n for _ in range(m)]
    visited[0][j] = 1
    q = deque([(0,j)])
    while q:
        a,b = q.popleft()
        for pos in range(4):
            nx = dx[pos]+a
            ny = dy[pos]+b
            if 0<= nx < m and 0 <= ny < n:
                if graph[nx][ny] == '0' and visited[nx][ny]== 0:
                    if nx == m-1:
                        return True
                    visited[nx][ny] = 1
                    q.append((nx,ny))
    return False
for _ in range(m):
    temp = list(str(input().rstrip()))
    graph.append(temp)
flag = False
for i in range(n):
    if graph[0][i] == '0':
        flag = bfs(i)
        if flag:
            break
if flag:
    print('YES')
else:
    print('NO')
