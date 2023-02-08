# 시간제한 1초
# 백트래킹을 사용하자.

n,m = map(int,input().split())

ans = []

def backtrack():
    # promising:
    if len(ans) == m:
        print(*ans)
        return
    for i in range(1,n+1):
        if i not in ans:
            ans.append(i)
        
            backtrack()
            ans.pop()
backtrack()
