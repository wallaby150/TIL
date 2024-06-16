N = int(input())
ans = [[' '] * 2 * N for _ in range(N)]


def recur(i, j, size):
    if size == 3:
        ans[i][j] = '*'
        ans[i+1][j-1] = ans[i+1][j+1] = '*'
        for k in range(-2, 3):
            ans[i+2][j+k] = '*'

    else:
        ds = size // 2
        recur(i, j, ds)
        recur(i + ds, j - ds, ds)
        recur(i + ds, j + ds, ds)


recur(0, N - 1, N)
for line in ans:
    print(''.join(line))
