n,m = map(int,input().split())

ans = []

def bt(idx):
    if len(ans)== m:
        print(*ans)
        return

    for i in range(idx,n+1):
        if i not in ans:
            ans.append(i)
            bt(i+1)
            ans.pop()

bt(1)
