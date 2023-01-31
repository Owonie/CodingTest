def solution(dartResult):
    point = {'S':1,'D':2,'T':3}
    stack = []
    dartResult = dartResult.replace('10','A')
    for i in dartResult:
        if i.isdigit() or i == 'A':
            stack.append(10 if i == 'A'else int(i))
        elif i in ('S','D','T'):
            num = stack.pop()
            stack.append(num ** point[i])
        elif i == '*':
            num = stack.pop()
            if len(stack):
                stack[-1] *= 2
            stack.append(num * 2)
        elif i == '#':
            stack[-1] *= -1
    return sum(stack)
