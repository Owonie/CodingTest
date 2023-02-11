# 시간제한 2초
# 시간 복잡도는 최소공배수 구하는 것보다 낮다
arr = list(map(int,input().split()))
i = 0

while(True):
    i += 1
    arr2 = []
    for _ in arr:
        arr2.append(i % _)
    if arr2.count(0) >= 3:
        print(i)
        break
