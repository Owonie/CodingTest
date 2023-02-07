# 시간 제한 1초 -> 2^20
# kC6 -> 2^ 13 < 1초
# 조합으로 풀어준다.

from itertools import combinations

while(True):
    arr = list(map(int,input().split()))
    if arr == [0]:
    # 그냥 0으로 설정하면 안된다
        break
    # 조합은 튜플형식으로 배열에 담긴다
    ans = list(combinations(arr[1:],6))
    for _ in ans:
        # 튜플을 배열로 전환시켜 정렬해준다.
        print(*_,sep='')
    print()
