import heapq
def solution(operations):
    heap = []
    for i in operations:
        if 'I' in i:
            heapq.heappush(heap,int(i[2:]))
        elif 'D -' in i :
            if len(heap) == 0:
                continue
            heapq.heappop(heap)
        elif 'D' in i :
            if len(heap) == 0:
                continue
            heap = heapq.nlargest(len(heap),heap)[1:]
            heapq.heapify(heap)
    if heap == []:
        return [0,0]

    
    return [max(heap),heap[0]]
