import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
ans = 0


def dfs(y, banned):
    global ans

    if y == N:
        ans += 1
        return

    for x in range(N):
        # 열 제외
        if x in banned[0] or y - x in banned[1] or y + x in banned[2]:
            continue

        banned[0].add(x)
        banned[1].add(y-x)
        banned[2].add(y+x)
        dfs(y+1, banned)
        banned[0].remove(x)
        banned[1].remove(y-x)
        banned[2].remove(y+x)


# 열, \, /
dfs(0, [set(), set(), set()])
print(ans)