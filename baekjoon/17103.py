import math

sieve = [True] * 1000001
def prime_list(num):
    for i in range(2,int(math.sqrt(num))+1):
        if sieve[i] == True:
            for j in range(2*i,num,i):
                sieve[j] = False
    return [i for i in range(2,num) if sieve[i] == True]

prime = []
arr = []
T = int(input())

# 케이스 숫자 입력
for i in range(T):
    arr.append(int(input()))
# 소수 리스트 구하기
prime = prime_list(1000001)

for i in arr:
    result = 0
    for j in prime:
        if i < j:
            break
        # 소수를 뺀 수가 소수일 시 result++
        if sieve[i-j] and i >= 2*j :
            result += 1
           
    print(result)


