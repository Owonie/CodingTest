N,L = map(int,input().split())

arr = list(map(int,input().split()))
arr.sort()
cnt = 1
start = arr[0]
for i in range(len(arr)):
    if arr[i] - start < L:
        if i == len(arr):
            cnt +=1
        continue
    start = arr[i]
    cnt+= 1
print(cnt)
