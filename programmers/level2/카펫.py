
def solution(brown, yellow):
    answer = []
    count = 1
    while(True):
        if 2*yellow/count + 2*count == brown -4:
            return [yellow/count+2,count+2]
        count += 1
    return answer
