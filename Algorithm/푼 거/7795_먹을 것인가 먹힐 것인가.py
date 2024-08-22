import sys
input = lambda: sys.stdin.readline().rstrip()


def solve():
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    last = -1
    ans = 0

    for a in A:
        for i in range(last + 1, M):
            b = B[i]
            if a > b:
                last = i
            else:
                break
        ans += last + 1
    return ans


T = int(input())
for _ in range(T):
    print(solve())
