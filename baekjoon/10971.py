# 시간 제한 2 초
# 그래프 입력
# 백트래킹 문제
# min_ans를 구하자

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [False] * n
visited[0] = True
min_ans = 1e9

def backtrack(depth,idx,ans):
    global min_ans
    if depth == n-1 and graph[idx][0] != 0:
        min_ans= min(min_ans,ans+graph[idx][0])
        return
    for i in range(n):
        if visited[i] == False and graph[idx][i] != 0:
            visited[i] = True
            backtrack(depth+1,i,ans+graph[idx][i])
            visited[i] = False
backtrack(0,0,0)
print(min_ans)
        
