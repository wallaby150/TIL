import sys
input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
colors = [[] for _ in range(K)]

for _ in range(N):
    x, y, c = map(int, input().split())
    colors[c-1].append((y, x))

answer = 4000001
tmp = []

def solve(depth):
    global answer

    if depth == K:
        hy, hx, ly, lx = -1000, -1000, 1000, 1000
        for dy, dx in tmp:
            hy = max(hy, dy)
            hx = max(hx, dx)
            ly = min(ly, dy)
            lx = min(lx, dx)

        s = abs((hy-ly)) * abs((hx - lx))
        answer = min(answer, s)
        if answer == 0:
            print(0)
            exit()
        return

    for dot in colors[depth]:
        tmp.append(dot)
        solve(depth + 1)
        tmp.pop()

solve(0)
print(answer)