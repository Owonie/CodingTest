num_list = [0,1]
def get_list():
    a = 0
    b = 1
    i = 2
    while(i < 100):
        if num_list[i-1]+num_list[i-2]>= 1000000000:
            return len(num_list)
        num_list.append(num_list[i-1]+num_list[i-2])
        i += 1
get_list()
T = int(input())
for i in range(T):
    ans = []
    n = int(input())
    while(n > 0):
        for j in range(len(num_list)):
                # 피보나치 수 중 가장 근접한 수 고르기
            if num_list[j] <= n:
                temp = num_list[j]
        n -= temp
        ans.append(temp)
    ans.sort()
    print(*ans)
