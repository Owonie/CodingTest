# 시간제한 1초
import sys
input = sys.stdin.readline

n = int(input())
arr1 = map(int,input().split())
m = int(input())
arr2 = map(int,input().split())

ans = {}

for _ in arr1:
    if _ in ans:
        ans[_] +=1
    else:
        ans[_] = 1
for i in arr2:
    if i in ans:
        print(ans[i],end=' ')
    else:
        print('0',end=' ')

