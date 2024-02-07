N, L, R, X = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = 0


def solve(idx, hap, low, high):
    global ans

    if idx == N or hap > R:
        if L <= hap <= R:
            if high - low >= X:
                ans += 1
        return

    solve(idx + 1, hap, low, high)

    # 처음일 때
    if not hap:
        solve(idx + 1, hap + nums[idx], nums[idx], nums[idx])
    else:
        solve(idx + 1, hap + nums[idx], low, nums[idx])

solve(0, 0, -1, -1)
print(ans)