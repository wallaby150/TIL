import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
nums = set(map(int, input().split()))
ans = 0


def dfs(now, idx):
    global ans

    if idx == N:
        if nums.issubset(now):
            ans += 1
        return

    for i in range(10):
        tmp = now.copy()
        tmp.add(i)
        dfs(tmp, idx + 1)


dfs(set(), 0)
print(ans)
