N, S = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0


def solve(idx, now):
    global ans

    if idx == N:
        return

    sub_sum = now + nums[idx]

    if sub_sum == S:
        ans += 1

    solve(idx + 1, sub_sum)
    solve(idx + 1, now)


solve(0, 0)
print(ans)
