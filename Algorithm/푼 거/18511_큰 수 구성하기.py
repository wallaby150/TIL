N, K = map(int, input().split())
nums = sorted(list(map(int, input().split())), reverse=True)
L = len(str(N))


def recur(now):
    if now > N:
        return 0

    togo = now
    for i in range(K):
        togo = max(recur(now * 10 + nums[i]), togo)

    return togo


ans = recur(0)
print(ans)
