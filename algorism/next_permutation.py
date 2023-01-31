N = int(input())
arr = list(map(int, input().split()))

def next_permutation():
    # 꼭대기 값 찾기
    i = N-1
    # 마지막 오름차순의 값이 꼭대기 값이다
    while( i > 0 and arr[i-1] >= arr[i]):
        i -= 1

    if i == 0:
        return False

    # 변경할 값 보다 다음으로 큰 값을 찾는다
    j = N - 1
    while ( arr[i-1] >= arr[j]):
        j -= 1
    arr[i-1], arr[j] = arr[j], arr[i-1]

    k = N - 1
    while(i<k):
        arr[i], arr[k] = arr[k], arr[i]
        i+= 1
        k -= 1
    return True

if not next_permutation():
    print(-1)
else:
    for i in range(N):
        print(arr[i], end=" ")
    
