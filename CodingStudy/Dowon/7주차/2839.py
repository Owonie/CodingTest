n = int(input())

ans = 0

while(n>=0):
    if n % 5==0:
        ans += n//5
        print(ans)
        break
    ans += 1
    n -= 3
else:
    print(-1)
