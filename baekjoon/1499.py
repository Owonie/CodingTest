# 시간제한 2초

def count_reverse_operations(A, B):
    n = len(A)
    reverse_ops = []
    end = n 
    # A와 B의 차이를 찾아 뒤집기 연산이 필요한 위치를 찾는다.
    for i in range(end):
        for _ in range(end):
            if A[-_] == B[-_]:
                end -= 1
                break
        if A[i] != B[i]:
            for j in range(1, end):
                if A[i] != A[n-j]:
                    end = end + 1 - j
                    # 뒤집기 연산을 수행한다.
                    for k in range(i, (end+1+i)//2):
                        A[k], A[end-k+i-1] = A[end-k+i-1], A[k]
                    reverse_ops.append((i, end-1))
                break

    for i in range(len(reverse_ops)-1):
        if reverse_ops[i][0] > reverse_ops[i+1][0]:
            return -1   
        if reverse_ops[i][1] < reverse_ops[i+1][1]:
            return -1
    return len(reverse_ops)


# 입력 예시
A = input().strip()
B = input().strip()
set_A = set(A)
set_B = set(B)
# 결과 출력
result = count_reverse_operations(list(A), list(B))
if set_A != set_B:
    print(-1)
else:
    print(result)

    
