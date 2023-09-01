import sys
input = lambda : sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    nums = []
    row_sum, col_sum = [0] * N, [0] * N
    for i in range(N):
        row = list(map(int, input().split()))
        row_sum[i] = sum(row)
        for j in range(N):
            col_sum[j] += row[j]
    
    # 연산 시작
    for _ in range(M):
        r1, c1, r2, c2, v = map(int, input().split())
        for i in range(r1-1, r2):
            row_sum[i] += v * (c2 - c1 + 1)

        for j in range(c1-1, c2):
            col_sum[j] += v * (r2 - r1 + 1)

    print(" ".join(map(str, row_sum)))
    print(" ".join(map(str, col_sum)))

