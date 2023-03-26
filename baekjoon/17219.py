# 시간제한 5초
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
arr = dict()

for _ in range(n):
    a, b = map(str,input().split())
    arr[a] = b

for _ in range(m):
    address = str(input().rstrip())
    print(arr[address])
