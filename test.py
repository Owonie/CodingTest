from itertools import permutations

n = int(input())
num = list(map(int,input().split()))
ans = 0
print(len(list(permutations(num,n))))
for _ in permutations(num,n):
    print(_)
    temp = 0
    for i in range(1,n):
        temp += abs(_[i]-_[i-1])
    ans = max(temp,ans)
print(ans)
