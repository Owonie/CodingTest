# 시간 제한 1초

# 30의 배수가 되는 조건-> 일의 자리수 = 0

# 각 자리의 숫자들을 더했을 때 3으로 떨어짐

# 가장 작은 수를 출력하기.

n = list(input())
n.sort(reverse=True)
ans =0

for i in n:
    ans += int(i)
if ans % 3 != 0 or n[-1] != '0':
    print(-1)
else:
    print(*n,sep='')
