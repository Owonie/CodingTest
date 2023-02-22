# 시간제한 1초

#  같은 수를 여러 번 골라도 되는 수열 : 중복 수열
# 10^7 < 10^8

n,m = map(int,input().split())

arr = list(map(int,input().split()))
arr.sort()
num = []
def backtrack(ans):
    if len(ans) == m:
        print(*ans)
        return
    temp = 0
    for i in range(n):
        if temp != arr[i]:
            ans.append(arr[i])
            temp = arr[i]
            backtrack(ans)
            ans.pop()
backtrack([])
