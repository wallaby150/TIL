import sys
input = lambda: sys.stdin.readline().rstrip()

K = int(input())
nums = list(map(int, input().split()))
possibles = set()


def dfs(idx, now):
    if now > 0:
        possibles.add(now)

    if idx == K:
        return

    dfs(idx+1, now + nums[idx])
    dfs(idx+1, now - nums[idx])
    dfs(idx+1, now)


dfs(0, 0)
cnt = 0
for i in range(1, sum(nums)):
    if i not in possibles:
        cnt += 1

print(cnt)