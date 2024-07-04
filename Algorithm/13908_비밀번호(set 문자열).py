import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
nums = set(input().split())
ans = 0


def dfs(now, idx):
    global ans

    if idx == N:
        tmp = set(now)
        if nums.issubset(tmp):
            ans += 1
        return

    for i in '0123456789':
        dfs(now + i, idx + 1)


dfs('', 0)
print(ans)
