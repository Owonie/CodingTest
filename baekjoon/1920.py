# 시간제한 1초

n= int(input())
arr =list(map(int,input().split()))
set_arr = set(arr)

m = int(input())
arr2 =list(map(int,input().split()))


for i in arr2:
    if i in set_arr:
        print(1)
    else:
        print(0)
