# 시간제한 1초

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(x,y,is_happy):
    if abs(x-end[0])+abs(y-end[1]) <= 1000:
        return True
    for i in range(n):
        if abs(x-arr[i][0])+abs(y-arr[i][1]) <= 1000:
            if visited[i] == 0:
                visited[i] = 1
                is_happy = dfs(arr[i][0],arr[i][1],is_happy)
    return is_happy
t= int(input())
for _ in range(t):
    n= int(input())
    start = list(map(int,input().split()))
    arr = []
    for i in range(n):
        a,b = map(int,input().split())
        arr.append((a,b))
    end = list(map(int,input().split()))
    visited = [0]*n
    is_happy = dfs(start[0],start[1],False)
    if is_happy == True:
        print("happy")
    else:
        print("sad")

