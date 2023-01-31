def solution(N, stages):
    dic = {}
    denominator = len(stages)
    for i in range(1,N+1):
        if denominator == 0:
            dic[i] = 0
        else:
            dic[i] = stages.count(i) / denominator
            denominator -= stages.count(i)
    return sorted(dic,key=lambda x:dic[x],reverse=True)

