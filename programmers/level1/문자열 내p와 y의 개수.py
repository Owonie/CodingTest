def solution(s):
    s1 = s.lower()
    if s1.count("p") == s1.count("y"):
        return True
    return False
