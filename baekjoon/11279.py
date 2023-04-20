# 시간제한 1초

import heapq
import sys

input = sys.stdin.readline
heap= []

n = int(input())

for _ in range(n):
    temp = int(input())
    if temp == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,-temp)
