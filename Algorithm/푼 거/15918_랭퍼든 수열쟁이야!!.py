N, X, Y = map(int, input().split())
visited = [0] * (N + 1)
ans = 0
a = [0] * (2 * N)
a[Y-1] = a[X-1] = Y - X - 1
visited[Y-X-1] = 1


def solve(arr, idx):
    global ans

    if idx == 2 * N:
        ans += 1
        return

    if arr[idx] != 0:
        solve(arr, idx + 1)

    else:
        for i in range(1, N+1):
            if visited[i] == 0:
                if idx + i + 1 < 2 * N:
                    if arr[idx + i + 1] == 0:
                        tmp = arr[:]
                        tmp[idx] = i
                        tmp[idx + i + 1] = i
                        visited[i] = 1
                        solve(tmp, idx + 1)
                        visited[i] = 0

solve(a, 0)
print(ans)