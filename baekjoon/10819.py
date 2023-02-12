# 시간제한 1초
# 시간 복잡도 8! < 10^8
# 단순히 순열로 풀어도 된다.
# 라이브러리 / 백트래킹 둘다 풀어보자.

# from itertools import permutations

n = int(input())
num = list(map(int,input().split()))
# ans = 0
# for _ in permutations(num,n):
    # temp = 0
    # for i in range(1,n):
        # temp += abs(_[i]-_[i-1])
    # ans = max(temp,ans)
# print(ans)
check = [False] * n
max_ans = 0
cnt = 0
def caculation(arr):
    global cnt
    ans = 0
    for i in range(1,n):
        ans += abs(arr[i]-arr[i-1])
    return ans
def backtrack(ans):
    global max_ans,cnt
    if len(ans) == n:
        max_ans = max(max_ans,caculation(ans))
        cnt+= 1
        return
    for i in range(n):
        if check[i] == False:
            check[i] = True
            ans.append(num[i])
            backtrack(ans)
            ans.pop()
            check[i] = False
backtrack([])
print(max_ans)

