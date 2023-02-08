# 시간제한 1초 시간복잡도 9! < 1초
from itertools import permutations


n = int(input())
# 답안 리스트 만들기
arr = list(permutations([1,2,3,4,5,6,7,8,9],3))
for _ in range(n):
    # 케이스 입력
    num,strike,ball = map(int,input().split())
    # 3자리 분리
    num = list(str(num))
    remove = 0
    for i in range(len(arr)):
        s = b = 0
        # 정답리스트에서 제외한 만큼 i를 빼줘야 루프 정상작동
        i -= remove
        for j in range(3):
            # 특정 숫자가 있는지
            if int(num[j]) in arr[i]:
                # 특정 위치에 있다면 스트라이크
                if j == arr[i].index(int(num[j])):
                    s += 1
                # 특정 위치에 없다면 볼
                else:
                    b += 1
        # 입력 상황과 다르다면 정답리스트에서 제거
        if s!= strike or b != ball:
            arr.remove(arr[i])
            remove += 1
print(len(arr))
