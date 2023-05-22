# 도원
# 시간제한 1초
import sys
input = sys.stdin.readline
from collections import deque

def bfs(node):
    queue = deque()
    queue.append(node)
    check[node] = 1

    while queue:
        temp = queue.popleft()

        for pos in graph[temp]:
            if check[pos] == 0:
                check[pos] = check[temp] + 1
                queue.append(pos)

for _ in range(int(input())):
    n = int(input())
    graph = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        v = int(input())
        graph[i].append(v)
    check = [0] * (n+1)
    bfs(1)
    print(check[n]-1 if check[n] > 0 else 0)
