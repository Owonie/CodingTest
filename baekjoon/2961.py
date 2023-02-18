# 시간제한 1초

# 신맛과 쓴맛의 차이 -> 브루트포스 -> 백트래킹

n = int(input())
arr = [list(map(int,input().split()))for _ in range(n)]
visited = [False] * n
min_ans = 1e9
def backtrack(depth,length,ans,idx):
    global min_ans,visited
    if depth == length:
        min_ans = min(abs(ans[1]-ans[0]),min_ans)
        return
    for i in range(idx,n):
        if visited[i] == False:
            visited[i] = True
            backtrack(depth+1,length,[ans[0]*arr[i][0],ans[1]+arr[i][1]],i)
            visited[i] = False
for j in range(1,n+1):
    backtrack(0,j,[1,0],0)
print(min_ans)
