# 시간제한 2초
import sys
input = sys.stdin.readline

r,c = map(int,input().split())
dx = [0,0,-1,1]
dy = [-1,1,0,0]
graph = []
is_safe = False
for _ in range(r):
    temp = list(map(str,input()))
    graph.append(temp)

for i in range(r):
    for j in range(c):
        if graph[i][j] == "W":
            for pos in range(4):
                nx = i+dx[pos]
                ny = j+dy[pos]
                if nx <= -1 or nx >= r or ny <= -1 or ny >= c:
                    continue
                if graph[nx][ny] == "S":
                    is_safe = True
                    break
if is_safe == True:
    print(0)
else:
    print(1)
    for i in range(r):
        for j in range(c):
            if graph[i][j] == ".":
                graph[i][j] ="D"
    for k in graph:
        print(''.join(k))

    
