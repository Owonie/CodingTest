# 시간제한 2초

import sys

input = sys.stdin.readline

n = int(input())
graph = [list(input()) for _ in range(n)]

visited = [[0] * n for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if graph[i][j] == "Y" or (graph[i][k] == "Y" and graph[k][j] == "Y"):
                visited[i][j] = 1

ans = 0
for _ in visited:
    ans = max(ans, sum(_))
print(ans)
