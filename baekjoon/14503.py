import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int,input().split())
start = list(map(int,input().split()))
graph = []
dy = [0,1,0,-1]
dx = [-1,0,1,0]
ans = 0

def dfs(i,j,d):
    global ans
    if graph[i][j] == 0:
        graph[i][j] = 2
        ans += 1
    
    for k in range(4):
        nd = (d + 3) % 4  
        nx, ny = i + dx[nd], j + dy[nd]

        if graph[nx][ny] == 0:
            dfs(nx, ny, nd)
            return
        d = nd
    nd = (d + 2) % 4
    nx, ny = i + dx[nd], j + dy[nd]
    
    if graph[nx][ny] == 1:
        return
    dfs(nx, ny, d)

for _ in range(n):
    graph.append(list(map(int,input().split())))

dfs(start[0], start[1], start[2])
print(ans)
