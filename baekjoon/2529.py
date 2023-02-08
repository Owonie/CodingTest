# 시간제한 1초
# 부등호 관계를 만족시키는 정수를 구해라
# 숫자는 0~9 개 부등호 갯수는 7개
# 0. 부등호 사이에 숫자를 넣는 기능
# 1. 부등호 관계를 만족시키는지?
# 2. 부등호 관계를 만족하면 정수로 출력
# 3. 0 부터 다시 시작

#최대 역으로 큰숫자부터 대입하기.
# 대입한 숫자의 리스트 
check = [False] * 10
max_ans = ""
min_ans = ""
k = int(input())
arr = list(map(str,input().split()))

def is_True(a, b, c):
    if c  == '<':
        return a < b
    else:
        return a > b
# 백트래킹 요소 -> 인덱스(탐색깊이) + 정수
def backtrack(idx, num):
    global max_ans, min_ans
    if idx == k+1:
        if len(min_ans) == 0:
            min_ans = num
        else:
            max_ans = num
    # return 꼭 해주자
        return
    
    for i in range(10):
        if check[i] == False:
            # 처음 시작했거나, 부등호 관계를 만족할때
            if idx == 0 or is_True(num[-1], str(i), arr[idx-1]):
                check[i] = True
                backtrack(idx+1,num + str(i))
                check[i] = False
    
backtrack(0,'')
print(max_ans)
print(min_ans)
