# 시간 제한 1초

# 30000 보다 같거나 작은 양의 정수
# 반례 n = 1 -> 1 1 0 1 
n = int(input())
max_arr = []
def get_list(num):
    global max_arr
    arr = [n]
    arr.append(num)
    # 이 부분은 for 문보단 while 문이 적절하다.
    for j in range(1,30000):
        if arr[j-1] - arr[j] < 0:
            break
        arr.append(arr[j-1] - arr[j])
    if len(max_arr) < len(arr):
        max_arr = arr[:]
for i in range(1,n+1):
    get_list(i)

print(len(max_arr))
print(*max_arr)
