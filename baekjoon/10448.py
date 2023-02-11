# 시간제한 1초
# 중복조합 돌려서 있는지 체크하기

from itertools import combinations_with_replacement

# 삼각수를 1000 까지 만들자.
arr = []
arr2 = []

def get_list():
    for i in range(1,100):
        if i*(i+1)//2 > 1000:
            break
        arr.append(i*(i+1)//2)
get_list()

# 삼각수의 리스트 길이 -> 45
# 중복조합의 가능수 -> 45^3 < 10^6 < 10^8

com = list(combinations_with_replacement(arr,3))

for _ in com:
    arr2.append(sum(_))
n = int(input())
for j in range(n):
    num = int(input())
    if num in arr2:
        print(1)
    else:
        print(0)
