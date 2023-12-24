import sys
input = lambda : sys.stdin.readline().rstrip()


def solve(idx):
    if len(tmp) == 6:
        print(*tmp)
        return

    for i in range(idx, K):
        if K - i + idx < 6:
            return
        tmp.append(S[i])
        solve(i + 1)
        tmp.pop()


while True:
    tmp = list(map(int, input().split()))
    if tmp == [0]:
        break

    K, S = tmp[0], tmp[1:]
    tmp = []
    solve(0)
    print()