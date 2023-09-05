# 시간제한 0.5초


# 각 숫자의 자릿수에 대한 합
# 마지막 자릿수의 합



n = int(input())
cnt = 0
for i in range(1,len(str(n))):
    cnt += 9 * (10 ** (i-1)) * i
cnt += (n - 10 ** (len(str(n))-1)+1) * len(str(n))
print(cnt)
