# 시간 제한 2초
# 10^7 < 10^8 -> for 문

n = int(input())
m = int(input())
if m != 0:
    broke = list(map(int,input().split()))
else:
    broke = []
ans = abs(100-n)

for i in range(0,1000000):
    num = str(i)
    for j in range(len(num)):
        if int(num[j]) in broke:
            break
        if j == len(num)-1:
            ans = min(ans,abs(int(num)-n)+len(num))

print(ans)
