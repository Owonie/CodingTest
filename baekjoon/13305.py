# 시간 제한 2초
# 싼 곳에서 많이사면 된다.
# 싼 곳에 가기 전까지 최소한의 기름을 사면 된다.

n = int(input())
road = list(map(int,input().split()))
city = list(map(int,input().split()))

idx = 0
price = city[0]
ans = 0
while(idx < n-1):
    if price >= city[idx+1]:
        ans += price*road[idx]
        price = city[idx+1]
        idx += 1
    else:
        ans += price*road[idx]
        idx += 1
print(ans)
    
