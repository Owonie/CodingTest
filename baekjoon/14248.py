# 시간제한 2초

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = list(map(int,input().split()))
s = int(input())
q = deque([])

def bfs(s,sv):
    q.append((s,sv))
    cnt = 1
    visited = [0] * n
    while q:
        idx, value= q.popleft()
        if idx + value < n:
            if visited[idx+value] == 0:
                visited[idx+value] = 1
                q.append((idx+value,graph[idx+value]))
                cnt += 1
        if idx - value > -1:
            if visited[idx-value] == 0:
                visited[idx-value] = 1
                q.append((idx-value,graph[idx-value]))
                cnt += 1
    return cnt

ans = bfs(s-1,graph[s-1])
print(ans)
