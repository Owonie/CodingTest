def solution(k,ranges):
    temp = k
    arr = []
    result = []
    cnt = 0
    while temp > 1:
        arr.append(temp)
        cnt += 1
        if temp % 2 == 0:
            temp /= 2
        elif temp % 2 != 0:
            temp = temp * 3 + 1
    arr.append(k)
    for _ in ranges:
        i,j = _[0],_[1]+k-1
        if i > j:
            result.append(-1)
        elif i == j:
            result.append(0)
        else:
            result.append(sum(arr[i:j]))
                
    return result
