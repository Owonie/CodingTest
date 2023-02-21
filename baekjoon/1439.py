# 시간 제한 2초
# 1로 split() 때려보자

n = input()
n1 = n.split('1')
n2 = n.split('0')
cnt1 = 0
cnt2 = 0
for i in n1:
    if i != '':
        cnt1 += 1
for j in n2:
    if j != '':
        cnt2 += 1
print(min(cnt1,cnt2))
