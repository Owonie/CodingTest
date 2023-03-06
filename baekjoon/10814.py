# 시간제한 3초
import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    a,b = map(str,input().split())
    arr.append((a,b))

arr.sort(key = lambda x:x[0])


for i in range(n):
    print(arr[i][0],arr[i][1])
