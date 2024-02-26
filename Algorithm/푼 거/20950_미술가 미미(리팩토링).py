import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
colors = [list(map(int, input().split())) for _ in range(N)]
target = list(map(int, input().split()))
ans = 255 * 3 + 1

def solve(now, idx):
    global ans

    if len(now) > 7:
        return

    if idx == N:
        if len(now) <= 1:
            return
        r, g, b = 0, 0, 0
        for c in now:
            r, g, b = r + c[0], g + c[1], b + c[2]
        r, g, b = r // len(now), g // len(now), b  // len(now)
        tmp = abs(target[0] - r) + abs(target[1] - g) + abs(target[2] - b)
        ans = min(tmp, ans)
        return

    now.append(colors[idx])
    solve(now, idx + 1)
    now.pop()
    solve(now, idx + 1)

solve([], 0)
print(ans)