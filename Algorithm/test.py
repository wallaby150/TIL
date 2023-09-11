import sys
input = lambda : sys.stdin.readline().rstrip()

L = int(input())
S = sorted(list(map(int, input().split())))
n = int(input())


def solve():
    for i in range(L):
        if S[i] == n:
            return 0
        elif S[i] > n:
            high = S[i]
            low = S[i - 1]
            break

    count = 0
    for j in range(low+1, n+1):
        # print(j)
        for k in range(n, high):
            if j == k == n:
                continue
            # print([j, k])
            count += 1
        # print('-----------------')
    return count


print(solve())


# high와 low의 차이가 1인 것도 고려하기

        

