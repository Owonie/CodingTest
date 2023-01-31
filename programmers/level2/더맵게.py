from heapq import heappush, heappop, heapify
def solution(scoville, K):
    array = scoville
    heapify(array)
    count = 0
    while(len(array) > 1):
        min_ = heappop(array)
        if min_ >= K:
            return count
        else:
            min_2 = heappop(array)
            heappush(array,min_+min_2*2)
            count+=1
    if array[0] >K:
        return count
    else:
        return -1
