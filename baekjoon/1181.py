# 시간제한 2초

n = int(input())
arr = []
for _ in range(n):
    temp = input()
    arr.append((temp,len(temp)))
set_arr = set(arr)
arr = list(set_arr)
arr.sort()
arr.sort(key =lambda x : x[1])
for i in range(len(arr)):
    print(arr[i][0])
