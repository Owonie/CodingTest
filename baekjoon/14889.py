# 시간 제한 2초
# 그래프 입력 / 방문 체크
# 그래프 순회 ( 2 중 for 문 )
# 나머지는 순열 백트래킹이랑 같다.

n = int(input())
checked = [False for _ in range(n)]
graph = [list(map(int,input().split()))for _ in range(n)]
ans = 1000

def backtrack(idx,depth):
    global ans
    if depth == n//2:
        start =0
        link =0
        # 그래프 순회
        for i in range(n):
            for j in range(n):
                if checked[i] and checked[j]:
                    start += graph[i][j]
                elif not checked[i] and not checked[j]:
                    link += graph[i][j]
        ans = min(ans,abs(start-link))
        return ans

    for i in range(idx,n):
        if not checked[i]:
            checked[i] = True
            backtrack(i+1,depth+1)
            checked[i] = False
backtrack(0,0)
print(ans)
