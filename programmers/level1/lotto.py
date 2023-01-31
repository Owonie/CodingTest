def solution(numbers):
    answer = 0
    arr = [1,2,3,4,5,6,7,8,9]
    arr2 = []
    for i in arr:
        if i not in numbers:
            arr2.append(i)
    print(arr2)
    for i in arr2:
        answer += i
    return answer
