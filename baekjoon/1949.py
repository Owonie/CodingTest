# 시간제한 2초

# 트리 총 합을 최대 -> 백트레킹 / dp
# 우수마을 끼리 인접 불가
# 미선정마을은 우수마을과 최소 하나 인접

import sys
input = sys.stdin.readline

n = int(input())
graph = [[0]*(n+1) for i in range(n+1)]

arr = list(map(int,input().split()))

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a][b] = b
    graph[b][a] = a

print(*graph)
