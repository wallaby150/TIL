import sys
input = lambda : sys.stdin.readline().rstrip()

L = int(input())
S = sorted(list(map(int, input().split())))
n = int(input())


def solve():
    low = high = 0

    for i in range(L):
        if S[i] == n:
            return 0
        elif S[i] > n:
            high = S[i]
            break
        else:
            low = S[i]

    count = 0
    for j in range(low+1, n+1):
        for k in range(n, high):
            if j == k == n:
                continue
            count += 1
    return count


print(solve())