# 시간제한 1초
# 시간복잡도 8*8*8*8 < 10^8
# 일단 순열 구현
# 비내림차순인지 확인하는 함수 만들기
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
