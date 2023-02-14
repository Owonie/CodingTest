# 시간 제한 2초
# 범위를 넘기면 1로 리셋
# 사실상 진수 변환이다.

e,s,m = map(int,input().split())
ans = 1
while(True):
    if (ans-e) % 15 == 0 and (ans-s) % 28 == 0 and (ans-m) % 19 == 0:
        break
    ans += 1
print(ans)
