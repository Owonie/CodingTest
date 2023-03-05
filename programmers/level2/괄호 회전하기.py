from collections import deque

def solution(s):
    q = deque(s)
    ans = 0
    for i in range(len(s)):
        if i > 0:
            temp = q.popleft()
            q.append(temp)
        s = []
        for _ in q:
            if s:
                if  _ == ']' and s[-1] == '[': 
                    s.pop()
                elif _ == '}'and s[-1] == '{'  :
                    s.pop()
                elif _ == ')' and s[-1] == '(' :
                    s.pop()
                else:
                    s.append(_)
            else:
                s.append(_)
        if len(s) == 0:
            ans += 1
    return ans
