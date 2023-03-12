# 시간제한 1초

while(True):
    n = list(map(int,input()))
    if n == [0]:
        break
    b = n[::-1]
    if n == b:
        print('yes')
    else:
        print('no')
