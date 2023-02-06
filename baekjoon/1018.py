# 제한시간 2초
# 교차로 칠해져 있기만 하면 된다
# 2가지 상황: w시작 b 시작
# O(n^2) 50 * 50 = 2500 < 1만 = 1초

# 루프를 돌려도 된다.

n,m = map(int,input().split())
board = []
for _ in range(n):
    board.append(input())
print(board)
