# 시간제한 2초
# N의 갯수 <= 20 -> 2^ 20 => 1초 조합을 써도 된다.

from itertools import combinations

result = 0
n,s = map(int,input().split())

arr = list(map(int,input().split()))

for i in range(1,len(arr)+1):
    com = list(combinations(arr,i))
    for j in com:
        if sum(j) == s:
            result += 1
print(result)
