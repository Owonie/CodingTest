T = int(input())
import math
for i in range(T):
    num = input()
    if '(' not in num:
        print("1/"+str(1/(float(num)))[:-2])
    else:
        arr = list(num)
        for j in range(len(arr)):
            if arr[j] == '(':
                if j == 2:
                    a = 0
                    b = num[j+1:-1]
                    nine = '9' * len(b)
                    b = int(b)
                else:
                    a = num[2:j]
                    b = num[j+1:-1]
                    nine = '9' * len(b)+'0' * len(a)
                    a = int(a)
                    b = int(b)      
        temp = num[2:].replace('(','')
        temp = temp.replace(')','')
        c = math.gcd(int(temp)-a,int(nine))
        print(str((int(temp) - a)/c)[:-2]+'/'+str(int(nine)/c)[:-2])
