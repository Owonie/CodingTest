# 시간제한 1초

# 삼각형 꼭짓점 -> x,y
# 삼각형 좌밑점 -> x+n/2, y-n/2
# 삼각형 우밑점 -> x+n/2, y+n/2
# 제일 큰 삼각형 -> n/2 변 크기가 3 이상일 때까지
# 좌표를 등록해준다.

n = int(input())
arr = [[' ' for _ in range(n*2)] for _ in range(n)]

def conq(x, y, index):
    if index <= 3:
        for i in range(3):
            for j in range(i+1):
                arr[x+i][y+j] = arr[x+i][y-j] = '*'
        arr[x+1][y] = ' '
        return
    mid = index // 2
    conq(x, y, mid)
    conq(x+mid, y-mid, mid)
    conq(x+mid, y+mid, mid)
    
conq(0, n-1, n)
for i in range(n):
    print("".join(arr[i]))
