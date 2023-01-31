import heapq
def solution(n, works):
    if sum(works) <=n:
        return 0
    answer = 0
    temp= 0
    heap = []
    for i in works:
        heapq.heappush(heap,-1*i)
    for i in range(n):
        temp = heapq.heappop(heap)
        temp += 1
        heapq.heappush(heap,temp)
    if min(heap) > 0:
        return 0
    for i in range(len(heap)):
        answer += heapq.heappop(heap) ** 2
    return answer
