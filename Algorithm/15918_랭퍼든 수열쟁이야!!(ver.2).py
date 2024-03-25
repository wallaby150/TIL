N, X, Y = map(int, input().split())
visited = [0] * (N + 1)
arr = [0] * (2 * N)
ans = 0
arr[Y-1] = arr[X-1] = Y - X - 1
visited[Y-X-1] = 1

def solve(idx):
    global ans

    if idx == 2 * N:
        ans += 1
        return

    if arr[idx] != 0:
        solve(idx + 1)

    else:
        for i in range(1, N+1):
            if visited[i] == 0:
                if idx + i + 1 < 2 * N:
                    if arr[idx + i + 1] == 0:
                        arr[idx] = i
                        arr[idx + i + 1] = i
                        visited[i] = 1
                        solve(idx + 1)
                        arr[idx] = 0
                        arr[idx + i + 1] = 0
                        visited[i] = 0

solve(0)
print(ans)