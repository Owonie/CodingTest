#  시간제한 2초

# 내림차순 정렬하기

n = int(input())
arr = []
ans = 0
for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse = True)

for i in range(n):
    if arr[i]-i <= 0:
        break
    ans += arr[i]-i
print(ans)
