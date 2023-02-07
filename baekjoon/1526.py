# 시간 제한 2초
# N 보다 작거나 같은 금민수 -> O(n)
# N <= 10^6 루프 하나

n = int(input())
for i in range(4,n+1):
    ans = str(n-i+4)
    if ans.count('4') + ans.count('7') == len(ans):
        print(n-i+4)
        break
