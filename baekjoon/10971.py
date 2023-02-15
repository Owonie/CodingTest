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
    # 하나의 도시빼고 모두 방문했을 때, 마지막 도시는 갈 수 없다면 break
    if depth == n-1 and graph[idx][0] != 0:
        min_ans= min(min_ans,ans+graph[idx][0])
        return
    # 도시를 하나씩 방문하기
    for i in range(n):
        # 방문을 안한 도시 / 방문을 할 수 있는 도시
        if visited[i] == False and graph[idx][i] != 0:
            visited[i] = True
            # ans는 더하지 말고, 인자로 넘겨주자
            backtrack(depth+1,i,ans+graph[idx][i])
            visited[i] = False
backtrack(0,0,0)
print(min_ans)
        
