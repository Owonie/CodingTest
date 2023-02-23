# 시간 제한 1초
# 총 F층 S -> G  
from collections import deque

F,S,G,U,D = map(int,input().split())

visited = [0] *(F+1)
# 특정 층수를 방문 했을 때 횟수를 저장한다.
def bfs():
    q = [S]
    while q:
        n = q.pop(0)
        if n == G:
            return visited[n]
        for _ in (n-D, n+U):
            if 0 <_<= F and visited[_]==0 and _ != S:
                visited[_] = visited[n]+1
                q.append(_)
    return "use the stairs"
result = bfs()
print(result)
