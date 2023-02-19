# 시간제한 1초
# 10장 -> 순열 10! < 10^8

from itertools import permutations

n = int(input())
k = int(input())
card = []

for i in range(n):
    card.append(str(input()))
temp = list(permutations(card,k))
ans = []
for j in range(len(temp)):
    num = ''
    for _ in range(k):
        num += str(temp[j][_])
    ans.append(int(num))
ans = set(ans)
print(len(ans))

