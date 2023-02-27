# 시간제한 1초
# 1. 치킨 거리재는 함수 2. 조합으로 치킨집 배치
from itertools import combinations

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

arr1 = []
arr2 = []
min_ans = 1e9

# 각각 그래프에서 집과 치킨집을 arr1,arr2에 저장해준다.
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            arr1.append([i,j])
        if graph[i][j] == 2:
            arr2.append([i,j])

# 치킨집의 분포 가능한 예를 arr3에 넣어준다.
arr3 = combinations(arr2,m)

for _ in arr3:
    ans = 0
    for i in arr1:
        length = 1e9
        for j in range(m):
            # 치킨거리를 하나씩 계산해준다. x ,y 좌표 거리구하기.
            length = min(length,abs(i[0]-_[j][0])+abs(i[1]-_[j][1]))
        ans+= length
    min_ans = min(min_ans,ans)
print(min_ans)
