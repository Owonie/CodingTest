# 시간 제한 2초
# 50^3 -> 루프돌며 문자 세기
arr1 = input()
arr2 = input()
cnt = 0
idx = 0
while idx <= len(arr1)-len(arr2):
    if arr2 == arr1[idx:idx+len(arr2)]:
        cnt += 1
        idx += len(arr2)
    else:
        idx += 1
print(cnt)
