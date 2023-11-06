import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
count = 0
base = 'antic'


def solve():
    global count, K

    # 기본으로 5개 이상이 되어야 함
    if K < 5:
        return
    K -= 5
    needs_dict = defaultdict(int)

    for _ in range(N):
        text = input()

        # 딱 8자인 경우
        if len(text) == 8:
            count += 1
            continue

        # 8자 이상인 경우
        middle = text[4:-4]
        flag = False
        needs = []

        for char in set(middle):
            if char not in base:
                flag = True
                needs.append(char)

        # 모든 글자가 base에 포함되는 경우
        if not flag:
            count += 1
            continue

        # 그렇지 않은 경우
        else:
            if K >= len(needs):
                needs.sort()
                tmp = ''.join(needs)
                needs_dict[tmp] += 1

    print(needs_dict)
    if needs_dict:
        f = sorted(needs_dict.values())
        for i in range(min(K, len(f))):
            count += f[i]


solve()
print(count)
