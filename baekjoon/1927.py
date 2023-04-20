# 시간제한 1초

import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
    temp = int(input())
    if temp == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,temp)
