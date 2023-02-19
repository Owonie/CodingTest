# 시간제한 2초

# i에 A명 총감독 B명 부감독 C명
# 너미저에 부감독 몇명 넣을지
n = int(input())
arr = list(map(int,input().split()))
b,c = map(int,input().split())
ans = 0
for i in arr:
    if i <= b:
        ans += 1
        continue
    if (i-b) % c == 0:
        ans += (i-b) // c +1
    else:
        ans += (i-b)//c+2

print(ans)

