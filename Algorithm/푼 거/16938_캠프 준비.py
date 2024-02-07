N, L, R, X = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = 0


def solve(idx, hap, choice):
    global ans

    if idx == N or hap > R:
        return

    solve(idx + 1, hap + nums[idx], choice + [nums[idx]])
    if len(choice) >= 1:
        if L <= hap + nums[idx] <= R:
            if nums[idx] - choice[0] >= X:
                ans += 1
    solve(idx + 1, hap, choice)


solve(0, 0, [])
print(ans)