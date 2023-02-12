# 시간제한 1초
# 시간복잡도 최대 50^4 < 100^4 = 10^8
# 그래프 모든 요소를 방문하기
# 아래로 / 우측으로 변경하고 다시 복구
# 하나를 기준으로 행 / 열 체크 ( 하나씩순회 )
ans = 0
def check(ans,graph):
    # 행 고정, 모든 요소 비교
    for i in range(n):
        cnt = 1
        for j in range(1,n):
            if graph[i][j] == graph[i][j-1]:
                cnt +=1
                ans = max(ans,cnt)
            else:
                cnt = 1
    # 열 고정, 모든 요소 비교
    for j in range(n):
        cnt = 1
        for i in range(1,n):
            if graph[i][j] == graph[i-1][j]:
                cnt +=1
                ans = max(ans,cnt)
            else:
                cnt = 1
    return ans

# 입력
n = int(input())
graph = [list(input()) for _ in range(n)]

# 아직 변환 주기 전 ans 초기화해주기:
ans = max(ans,check(0,graph))

for i in range(n):
    for j in range(1,n):
        # 두개 교환 -> 체크 -> 복구 행고정
        graph[i][j],graph[i-1][j] = graph[i-1][j],graph[i][j]
        ans = max(ans,check(ans,graph))
        graph[i][j],graph[i-1][j] = graph[i-1][j],graph[i][j]
for j in range(n):
    for i in range(1,n):
        # 두개 교환 -> 체크 -> 복구 열고정
        graph[i][j],graph[i][j-1] = graph[i][j-1],graph[i][j]
        ans = max(ans,check(ans,graph))
        graph[i][j],graph[i][j-1] = graph[i][j-1],graph[i][j]
print(ans)       
