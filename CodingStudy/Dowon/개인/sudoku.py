# 시간제한 1초

# key는 blank를 깊이로 취급한다는 것이다.
import sys
input = sys.stdin.readline

graph = []
blank = []
flag = True
for i in range(9):
    graph.append(list(map(int,input().split())))
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i,j))

def promising(x,y,value):
    for i in range(9):
        if graph[x][i] == value:
            return False
        if graph[i][y] == value:
            return False
    for i in range(3):
        for j in range(3):
            if graph[x//3*3+i][y//3*3+j] == value:
                return False
    return True


def dfs(i):
    global flag
    if flag:
        if i == len(blank):
            flag = False
            for yalo in graph:
                print(*yalo)
            exit(0)
        for j in range(1,10):
            x = blank[i][0]
            y = blank[i][1]
            if promising(x,y,j):
                graph[x][y] = j
                dfs(i+1)
                graph[x][y] = 0
dfs(0)

