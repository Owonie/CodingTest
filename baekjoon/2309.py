# 9개의 숫자에서 7개의 숫자의 합이 100이 되는
# 수의 배열을 오름차순으로 출력하기
# 시간 제한 2초 -> 2억
# 조합을 사용했을 때 2^9 < 2억 조합을 사용하자
from itertools import combinations

arr = []
for _ in range(9):
    arr.append(int(input()))

ans = list(combinations(arr,7))
for i in ans:
    if sum(i) == 100:
        temp = list(i)
        temp.sort()
        print(*temp)
        # break를 넣지 않으면 정답이 여러개 나올 수 있다.
        break
