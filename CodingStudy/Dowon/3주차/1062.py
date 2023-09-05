# 시간제한 1초

# n개의 단어개수 k개의 알파벳
# antic 는 무조건 들어가야하기에 알파벳은 5 이상이어야함
# set으로 각 단어를 다 담아주기
# 조합으로 완탐 -> lenth에 적합하면 카운트

from itertools import combinations

n,k = map(int,input().split())

if k < 5:
    print(0)
else:
    words = [input() for _ in range(n)]
    alphabets = set()
    for word in words:
        alphabets.update(set(word[4:-4]))

    combs = list(combinations(alphabets, k-5))
    # 중간 문자 중 조합으로 돌려주기

    max_count = 0
    for comb in combs:
        comb_set = set(comb)
        comb_set.update(['a', 'n', 't', 'i', 'c'])
        count = sum(1 for word in words if set(word) <= comb_set)
        max_count = max(max_count, count)

    print(max_count)
