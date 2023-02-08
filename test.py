n,m = map(int,input().split())
arr = []
def backtrack(idx):
    # promising:
    if idx == m+1:
        print(*arr)
        return
    for i in range(1,n+1):
        if i not in arr:
            arr.append(i)
            idx += 1
            backtrack(idx)
            arr.pop()
backtrack(0)
