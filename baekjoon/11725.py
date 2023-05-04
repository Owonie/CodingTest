# 시간제한 1초
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

def dfs(idx):
    for node in graph[idx]:
        if visited[node] == 0:
            visited[node] = idx
            dfs(node)
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(1)

for i in range(2,n+1):
    print(visited[i])
