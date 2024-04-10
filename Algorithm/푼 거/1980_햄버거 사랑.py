N, M, T = map(int, input().split())


def solve():
    ans_H, ans_C = 0, T
    b, s = max(N, M), min(N, M)

    for i in range(T//s, -1, -1):
        rest = T - s * i
        for j in range(rest//b, -1, -1):
            if rest - j * b == 0:
                return i + j, 0

            if ans_C > rest - j * b:
                ans_H = i + j
                ans_C = rest - j * b

    return ans_H, ans_C


print(*solve())