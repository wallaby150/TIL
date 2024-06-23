import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())


def solve(now, idx, target):
    if idx == target:
        if eval(now.replace(' ', '')) == 0:
            print(now)
        return

    for char in ' +-':
        solve(now + char + str(idx+1), idx+1, target)

    return


for _ in range(T):
    N = int(input())
    solve('1', 1, N)
    print()
