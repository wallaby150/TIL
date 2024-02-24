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
        for i in now:
            r += colors[i][0]
            g += colors[i][1]
            b += colors[i][2]
        r //= len(now)
        g //= len(now)
        b //= len(now)
        tmp = abs(target[0] - r) + abs(target[1] - g) + abs(target[2] - b)
        ans = min(tmp, ans)
        return

    now.append(idx)
    solve(now, idx + 1)
    now.pop()
    solve(now, idx + 1)

solve([], 0)
print(ans)