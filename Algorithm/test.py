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

    if depth > 1:


    if depth == K:
        pass
        return

    for dot in colors[depth]:
        tmp.append(dot)
        solve(depth + 1)
        tmp.pop()


solve(0)