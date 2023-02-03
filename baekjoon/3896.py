sieve = [True] * 1299710
def prime_list(n):
    m = int(n ** 0.5)
    for i in range(2,m+1):
        if sieve[i] == True:
            for j in range(2*i, n, i):
                sieve[j] = False
prime_list(1299710)
T = int(input())

for _ in range(T):
    num = int(input())
    if sieve[num] == True:
        print(0)
        continue
    i = num-1
    j = num+1
    while(sieve[i]== False):
        i -= 1
    while(sieve[j]==False):
        j += 1
    print(j-i)
