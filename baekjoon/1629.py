# 시간 제한 0.5
# 지수법칙 : a^(n+m) = a^n * a^m
# 모듈러 성질 :  (a*b)%c = (a%c * b%c)%c
a,b,c = map(int,input().split())

def multi(a,n):
    if n == 1:
        return a%c
    else:
        temp = multi(a,n//2)
        if n % 2 == 0:
            return temp**2 % c
        else:
            return temp**2*a%c
print(multi(a,b))
