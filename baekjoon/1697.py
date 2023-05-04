# 시간제한 2초
from collections import deque

n,k = map(int,input().split())
graph=[0]*100001
q= deque([n])
def bfs():
    global k
    while q:
        idx = q.popleft()
        if idx == k:
            print(graph[idx])
            break
        for nx in (idx+1,idx-1,idx*2) :
            if 0 <= nx <= 100000 and graph[nx] == 0 :
                q.append(nx)
                graph[nx] = graph[idx]+1
    return
bfs()
