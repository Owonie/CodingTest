# 시간 제한 0.5초
# 누적합 문제

# 누적합을 구하여 M이 되는 경우를 출력하면 된다.

import sys
input = sys.stdin.readline
arr = []
n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr2 = [0]*n
arr2[0] = arr[0]
for i in range(1,n):
    arr2[i] = arr[i]+arr2[i-1]
cnt = 0
end = 0
for start in range(n):
    while arr2[end]-arr2[start] < m and end < n-1:
        end += 1
        if end == n:
            break
    if arr2[end] - arr2[start] == m:
        cnt += 1
for j in range(n):
    if arr2[j] == m:
        cnt += 1
print(cnt)
