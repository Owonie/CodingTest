# 시간제한 1초

n,m = map(int,input().split())
check = [False] * n
  
def backtrack(index,ans):
    if len(ans) == m:
        print(*ans)
        return
    for i in range(index,n+1):
        ans.append(i)
        backtrack(i,ans)
        ans.pop()
backtrack(1,[])
