# 시간제한 2초

n,m = map(int,input().split())
print(0,1)
start = 0
end = 1
cnt = m-2

for i in range(n-2):
    if cnt >= 0:
        end += 1
        cnt -= 1
        print(1,end)
        continue
    end += 1
    start = end - 1
    print(start,end)
