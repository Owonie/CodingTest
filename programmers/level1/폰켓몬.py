def solution(nums):
    answer = 0
    dic = {}
    for i in nums:
        if i not in dic:
            dic[i]=1
            continue
        dic[i] += 1
    if len(dic) >= len(nums)/2:
        return int(len(nums)/2)
    else:
        return int(len(dic))
