# 시간 제한 1초

# 최소한의 변경으로 오름차순으로 만들기

n = int(input())
arr = []
cnt = 0
for i in range(n):
    arr.append(int(input()))
for _ in range(n-1,0,-1):

    if arr[_] <= arr[_-1]:
        cnt += arr[_-1]-arr[_]+1
        arr[_-1] = arr[_]-1

print(cnt)
