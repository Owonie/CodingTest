# 시간제한 2초
# 216 -> a + 각 자리수 더하기
# i 에서 n 자리 까지 하나씩 더하기
# 100만 < 2초

num = int(input())
ans = 0

for i in range(1,int(num)):
    n = list(map(int, str(i)))
    if sum(n) + i == num:
        ans = i
        break
print(ans)
