# 시간 제한 2초
# 병렬 연결시 각 로프에 가해지는 힘 w/k
# n값부터 차례대로 로프의 갯수를 줄여간다.

n = int(input())
arr = []
ans = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

for i in range(n):
    ans.append(arr[-i-1]*(i+1))
print(max(ans))
    
