# 시간제한 1초
# 짝수 1 2 1 2 반복
# 홀수 1 2 1 2 3

n = int(input())

if n % 2  == 0:
    arr = [1,2]*(n//2)
else:
    arr = [1,2]*((n-1)//2)
    arr.append(3)
print(*arr)
