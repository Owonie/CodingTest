# 시간제한 1초
def check(n,m):
    cnt = 0
    for i in range(n,m+1):
        arr = set(str(i))
        if len(arr) == len(str(i)):
            cnt += 1
    print(cnt)
while(True):
    try:
        n,m = map(int,input().split())
    except:
        break
    check(n,m)
    
