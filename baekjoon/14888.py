# 시간 제한 2초

# 백 트래킹 

n = int(input())
arr = list(map(int,input().split()))
sign = list(map(int,input().split()))
min_ans = 1e9
max_ans = -1e9
def backtrack(depth,plus,minus,multi,divide,ans):
    global min_ans,max_ans
    if depth == n:
        min_ans = min(ans,min_ans)
        max_ans = max(ans,max_ans)
    if plus > 0:
        backtrack(depth+1,plus-1,minus,multi,divide,ans+arr[depth])
    if minus > 0:
        backtrack(depth+1,plus,minus-1,multi,divide,ans-arr[depth])
    if multi > 0:
        backtrack(depth+1,plus,minus,multi-1,divide,ans*arr[depth])
    if divide > 0:
        backtrack(depth+1,plus,minus,multi,divide-1,int(ans/arr[depth]))
            
backtrack(1,sign[0],sign[1],sign[2],sign[3],arr[0])
print(max_ans)
print(min_ans)
