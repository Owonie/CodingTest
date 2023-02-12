# 시간제한 2초
# 최대 50 * 50
# A가 B에 제일 많이 중복되는 구간을 찾자.
# 찾은 후 비교하여 차이를 구하면 답.

A,B = map(str,input().split())
ans = len(B)
for i in range(len(B)-len(A)+1):
    cnt = 0
    for j in range(len(A)):
        if A[j] != B[j+i]:
            cnt += 1
    ans = min(ans,cnt)
print(ans)
