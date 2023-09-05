import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
q = deque()

ans = []
cnt = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(n, m):
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    q.append((0, 0))
    total = 0
    while q:
        x, y = q.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0 <= nx < n and 0 <= nx < m:
                if arr[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                elif arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    total += 1
                    visited[nx][ny] = 1
    return total

while True:
    ans.append(bfs(n, m))
    cnt += 1
    if sum(map(sum, arr)) == 0:  # 남아있는 치즈가 없으면 break
        break




print(cnt)
print(ans[-1])   
