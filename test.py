import math
while(True):
    m,n = map(int,input().split())
    print('m:',m,'n:',n,'gcd:',math.gcd(m,n),'gcd2:',math.gcd(int('1'*m),int('1'*n)))
