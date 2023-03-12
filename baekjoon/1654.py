# 시간제한 2초

k,n = map(int,input().split())

arr = []
for _ in range(k):
    temp = int(input().strip())
    arr.append(temp)

short = 1
long = max(arr)
while short <= long:
    temp = (short+long)//2
    cnt = 0
    for i in arr:
        cnt+= i//temp
    if cnt >= n:
        short = temp +1
    else:
        long = temp -1
print(long)
