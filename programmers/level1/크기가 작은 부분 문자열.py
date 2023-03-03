def solution(t, p):
    answer = 0
    idx = 0 
    while(idx <= len(t)-len(p)):
        if int(p) >= int(t[idx:idx+len(p)]):
            answer += 1
        idx += 1

    return answer
