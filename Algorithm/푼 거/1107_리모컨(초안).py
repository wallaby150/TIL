N = int(input())
M = int(input())
if M:
    nums = set(map(str, range(10))) - set(map(str, input().split()))

ans = abs(N - 100)
l = len(str(N))

def solve(now):
    global ans

    if len(now) > l + 1:
        return

    if now:
        ans = min(ans, abs(int(now) - N) + len(now))

    for num in nums:
        if not now and num == 0:
            continue
        solve(now + num)

if M:
    solve('')
    print(ans)
else:
    print(min(ans, len(str(N))))