import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(i,j):
    visited[j][i] = 1
    for idx in range(4):
        nx = dx[idx]+i
        ny = dy[idx]+j
        if 0<= nx< n and 0 <= ny < n and visited[ny][nx] == 0 and graph[ny][nx] > rain:
            dfs(nx,ny)
ans = 1
for rain in range(1,100):
    cnt = 0
    visited = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[j][i] == 0 and graph[j][i] > rain:
                dfs(i,j)
                cnt += 1
    ans = max(ans,cnt)
print(ans)
