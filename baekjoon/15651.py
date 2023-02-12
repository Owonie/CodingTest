# 시간제한 1초
# 죽음의 n과/m 시리즈 (3)
# 수 입력 받으면 백 트래킹으로 방문
# 인덱스가 중복할 수 있음
# 같은 출력은 안된다.
# 일단 1~n 까지의 가능한 배열을 출력하는 순열을 구현하자

n,m = map(int,input().split())
ans = []
def backtrack(idx,ans):
    if idx == m:
        print(*ans)
        return
    # 전 숫자
    for i in range(n):
        # 다음 숫자
        ans.append(i+1)
        backtrack(idx+1,ans)
        ans.pop()
                        

backtrack(0,ans)
