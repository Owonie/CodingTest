# 시간제한 1초

ans = 0
temp = 0
# 10개의 버섯 입력
for _ in range(10):
    mush = int(input())
    temp = ans
    ans += mush
    if ans == 100:
        print(100)
        break
    if ans > 100:
        if abs(100-temp) >= abs(100-ans):
            print(ans)
            break
        else:
            print(temp)
            break
if ans < 100:
    print(ans)
