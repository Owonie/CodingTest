# 시간제한 2초
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = dict()
for i in range(1,n+1):
    temp = input().rstrip()
    arr[i] = temp
    arr[temp] = i

for j in range(m):
    temp = input().rstrip()
    if temp.isdigit():
        print(arr[int(temp)])
    else:
        print(arr[temp])
