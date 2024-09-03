import sys
input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
colors = [[] for _ in range(K)]

for _ in range(N):
    x, y, c = map(int, input().split())
    colors[c-1].append((y, x))

answer = 4000001


def solve(depth, hy, ly, hx, lx):
    global answer

    if depth == K:
        s = abs((hy - ly)) * abs((hx - lx))
        answer = min(answer, s)
        if answer == 0:
            print(0)
            exit()
        return

    for ny, nx in colors[depth]:
        hy2 = max(hy, ny)
        hx2 = max(hx, nx)
        ly2 = min(ly, ny)
        lx2 = min(lx, nx)

        area = abs((hy2 - ly2)) * abs((hx2 - lx2))
        if area < answer:
            if depth == K:
                answer = min(answer, area)
                if answer == 0:
                    print(0)
                    exit()
            else:
                solve(depth + 1, hy2, ly2, hx2, lx2)
    return


solve(0, -1000, 1000, -1000, 1000)
print(answer)