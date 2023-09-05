# 시간제한 1초

# 50 x 50 -> 2중 for 문 x
# 1. land -> 완탐 -> 시간초과
# 2. 백트레킹 ? dfs로 구현하기 -> 최단거리 x
# 3. 가지치기 -> 시작점 미리 색출하기

import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
graph = []
land = []

for i in range(n):
    graph.append(list(map(str,input().rstrip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def findStartPoint(x,y):
    cnt = 0
    for direct in range(4):
        nx = x + dx[direct]
        ny = y + dy[direct]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 'L':
                cnt += 1
    if cnt == 1:
        return True
    else:
        return False

def bfs(i,j):
    visited = [[0]*m for _ in range(n)]
    visited[i][j] = 1
    q = deque([])
    q.append((i,j,0))
    cnt = 0
    while q:
        x,y,z = q.popleft()
        for pos in range(4):
            nx = x + dx[pos]
            ny = y + dy[pos]
            if 0<= nx < n and  0 <= ny < m:
                if graph[nx][ny]== 'L' and visited[nx][ny] == 0:
                    visited[nx][ny] =1
                    cnt = max(cnt,z+1)
                    q.append((nx,ny,z+1))
    return cnt

ans = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            ans = max(ans,bfs(i,j))
print(ans)




# in land? 로 prunning -> 'W'일 경우 가지치기
# land * land -> 50 * 50
# 시작점을 어떻게 지정할지?
# 두 거리가 최단 거리이면서 가장 가까워야한다 -> BFS?

# 시작점의 가능성이 높은 지점을 미리 색출하기
# 오로지 하나의 길에만 L로 연결되어있는 지점은
# 시작점일 가능성이 다분하기에 탐색 빈도를 단축할 수 있다.
# 만약 모든 그래프가 L이라면 -> 0

# 덩어리로 모여있는 L은 처리가 불가능하다.
# 단순하게 start 지점을 모아주는 처리 자체가
# L이 압도적으로 많을 땐 오히려 시간복잡도를 올려서
# 좋은 방식은 아니다. 연구실 처럼 소수의 시작지점이
# 있는 문제에서만 사용하도록 하자.
