import sys
input = lambda : sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    W = input()
    K = int(input())

    count = {}

    # 각 문자의 개수 세기
    for char in W:
        count[char] = count.get(char, 0) + 1

    check = False
    highest = -1
    lowerest = len(W)

    char_dict = {}
    # 문자열을 돌면서
    for i in range(len(W)):
        # 해당 문자가 K개 이상인지 확인
        if count[W[i]] < K:
            continue

        # k개 이상인 게 있으므로 정답이 있음
        check = True
        # 문자를 키로, 인덱스 리스트를 밸류로 갖도록 추가.
        char_dict[W[i]] = char_dict.get(W[i], []) + [i]

    # 인덱스 위치를 기준으로 각 문자가 k개 들어가는 걸 확인하며 최소와 최대를 갱신
    for key, values in char_dict.items():
        for i in range(len(values) -K +1):
            highest = max(highest, values[i+K-1] - values[i]+1)
            lowerest = min(lowerest, values[i+K-1] - values[i]+1)

    if check:
        print(lowerest, highest)
    else:
        print(-1)