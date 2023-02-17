# 시간 제한 1초

# 4: 1212 5: 12132 7 1212132
# 짝수인 경우 12121212
# 홀수인 경우 121212121232

n = int(input())
arr = []
if n % 2 == 0:
    for i in range(n//2):
        arr.append(1)
        arr.append(2)
    print(*arr)
else:
    for i in range((n-2)//2):
        arr.append(1)
        arr.append(2)
    arr.append(1)
    arr.append(3)
    arr.append(2)
    print(*arr)
