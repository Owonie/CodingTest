# 시간제한 1초
import sys
from collections import deque 
input = sys.stdin.readline

m,n,h = map(int,input().split())
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]
q = deque()
graph = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]

def bfs():
    while q:
        z,x,y = q.popleft()
        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]
            if -1<nx<n and -1<ny<m and -1<nz<h:
                if graph[nz][nx][ny]==0:
                    graph[nz][nx][ny] = graph[z][x][y]+1
                    q.append((nz,nx,ny))
ans = 0
cnt = -2
flag = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] ==1:
                q.append((i,j,k))

bfs()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] ==0:
                flag = 1
            cnt = max(cnt,graph[i][j][k])
if flag == 1:
    print(-1)
elif cnt == -1:
    print(0)
else:
    print(cnt-1)
            
