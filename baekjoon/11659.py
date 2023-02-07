# 시간제한 1초
# n => 10^6  m=> 10^6
# 최대시간 => 10^12 > 10^8 ~= 1초
# 루프 x  누적합 기법 o

import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr2 = [0] * n
arr2[0] = arr[0]
for _ in range(1,n):
    arr2[_] = arr[_]+arr2[_-1]
for i in range(m):
    j,k = map(int,input().split())
    if j == 1:
        print(arr2[k-1])
    else:
        print(arr2[k-1]-arr2[j-2])

