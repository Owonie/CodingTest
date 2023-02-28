# 시간 제한 1초

n = int(input())
arr = list(map(int,input().split()))
max_ans = 0
def backtrack(w,ans):
    global max_ans
    if len(w) == 2:
        max_ans = max(max_ans,ans)
        return
    for i in range(1,len(w)-1):
        backtrack(w[:i]+w[i+1:], ans + w[i-1]*w[i+1])
backtrack(arr,max_ans)
print(max_ans)
