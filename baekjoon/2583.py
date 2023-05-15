# 시간제한 1초
import sys
from collections import deque
input = sys.stdin.readline
m,n,k = map(int,input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
graph = [[0]*n for _ in range(m)]
for _ in range(k):
    a,b,c,d = map(int,input().split())
    for i in range(a,c):
        for j in range(b,d):
            graph[j][i] = 1


def bfs(i,j):
    cnt = 0
    q = deque([(i,j)])
    while q:
        a,b = q.popleft()
        for pos in range(4):
            nx = a + dx[pos]
            ny = b + dy[pos]
            if 0<= nx < n and 0<= ny < m:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = 1
                    cnt += 1
                    q.append((nx,ny))
    return cnt
ans = []
cnt = 0
for i in range(n):
    for j in range(m):
        if graph[j][i] == 0:
            temp = max(1,bfs(i,j))
            ans.append(temp)
            cnt += 1
print(cnt)
ans.sort()
print(*ans)

