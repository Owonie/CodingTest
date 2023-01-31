import sys
input = sys.stdin.readline

def next_permutation(arr):
    i = len(arr) -2
    # 꼭대기 값 찾기
    while i >= 0 and arr[i] >= arr[i+1]:
        i -= 1
    # 정렬 완료
    if i == -1:
        return False
    # 꼭대기 앞 값보다 다음으로 큰 값 찾기 
    j = len(arr) - 1
    while arr[i] >= arr[j]:
        j -= 1
    arr[i], arr[j] = arr[j], arr[i]
    # 교환 후 꼭대기 값 뒤에 오름차순으로 정렬
    result = arr[:i+1]
    result.extend(list(reversed(arr[i+1:])))
    return result

T = int(input())
for _ in range(T):
    Case = list(input().rstrip())
    ans = next_permutation(Case)
    if not ans:
        print("".join(Case))
    else:
        print("".join(ans))
