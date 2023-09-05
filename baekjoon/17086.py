# 시간제한 2초

import sys
from collections import deque
input = sys.stdin.readline

# 1. 그래프 선언
# 2. dx, dy 선언
# 3. 안전거리 구하기 - dfs
# 4. 안전거리에서 가장 큰 값 출력
## 모든 칸을 방문하면서 안전거리를 구한다 - 2중 for 문

#1
graph = []
n,m = map(int,input().split())

for _ in range(n):
    temp = list(map(str,input().split()))
    graph.append(temp)

dx = [0,0,-1,1,-1,1,-1,1]
dy = [-1,1,0,0,1,-1,-1,1]

def bfs(i,j,k):
    q = deque([(i,j,k)])
    visited = [[0]*m for _ in range(n)]
    while q:
        x,y,cnt = q.popleft()
        for pos in range(8):
            nx = dx[pos] + x
            ny = dy[pos] + y
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0:
                    if graph[nx][ny] == '1':
                        return cnt+1
                    else:
                        visited[nx][ny] = 1
                        q.append((nx,ny,cnt+1))
    return cnt
ans = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == '0':
            ans.append(bfs(i,j,0))
print(max(ans))

#  헷갈렸던 부분:
# 0과1로 이루어진 그래프라 map - str로 받아주고
# graph[i][j] == '1' 에서 꼭 따옴표를 넣어줘야한다.
# n이 줄의 갯수여서 2중 for문을 쓸 때 순서를 그대로했다.
