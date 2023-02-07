# 시간제한 1초 1억 1
# n <= 10^5 => 에라토스테네스의 체

# 소수 리스트 구하기
sieve = [True] * 1299710

#에라토스테네스의 체
def prime_list(n):
    m = int(n ** 0.5)
    for i in range(2,m+1):
        if sieve[i] == True:
            for j in range(2*i, n, i):
                sieve[j] = False
                
prime_list(1299710)

# 케이스 입력
T = int(input())

for _ in range(T):
    num = int(input())
    # 자기 자신이 소수일 경우 소수사이수열 x
    if sieve[num] == True:
        print(0)
        continue
    # 앞 뒤로 확장
    i = num-1
    j = num+1
    # 소수가 나올 때 까지 앞뒤로 확장한다.
    while(sieve[i]== False):
        i -= 1
    while(sieve[j]==False):
        j += 1
    # 소수사이수열의 길이 출력
    print(j-i)
