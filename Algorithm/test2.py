import sys

input = lambda: sys.stdin.readline().rstrip()

L = int(input())
S = sorted(list(map(int, input().split())))
n = int(input())


def solve():
    if n in S:
        return 0

    low = high = 0

    for i in range(L):
        if S[i] < n:
            low = S[i]
        elif S[i] > n:
            high = S[i]
            break

    count = 0
    for j in range(low + 1, n):
        for k in range(n + 1, high):
            count += 1

    return count


print(solve())
