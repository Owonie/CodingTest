import math
n,m = map(int,input().split())
temp = math.factorial(n-m)
n = math.factorial(n)
m = math.factorial(m)

print(n//(m*temp))
