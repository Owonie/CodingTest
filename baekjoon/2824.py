import math
def multiply(arr):
    ans = 1
    for n in arr:
        if ans == 0:
            return 0
        ans *= n
    return ans 

N = int(input())
arr1 = list(map(int, input().split())) 

M = int(input())
arr2 = list(map(int, input().split())) 

a = multiply(arr1)
b = multiply(arr2)

ans = str(math.gcd(a,b))
if len(ans) > 9:
    print(ans[-9:])
else:
    print(ans)

