# 시간제한 2초

t = int(input())
for _ in range(t):
    s = [1, 1, 2, 4]
    n = int(input())
    for i in range(4, n + 1):
        s.append(s[i - 1] + s[i - 2] + s[i - 3] + s[i - 4])
    print(s[n])
