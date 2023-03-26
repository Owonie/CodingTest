# 시간제한 1초

while True:
    temp = input()
    s = []
    if temp == ".":
        break
    for i in temp :
        if i == '[' or i == '(':
            s.append(i)
        elif i == ']':
            if len(s) != 0 and s[-1] == '[':
                s.pop()
            else:
                s.append(']')
                break
        elif i == ')':
            if len(s) != 0 and s[-1] == '(':
                s.pop()
            else:
                s.append(')')
                break
    if len(s) == 0:
        print('yes')
    else:
        print('no')
