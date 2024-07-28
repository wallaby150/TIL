import sys
input = lambda: sys.stdin.readline().rstrip()


def dfs(idx):
    global ans

    if idx == N:
        if check():
            ans = "YES"
            print(ans)
            for i in range(N):
                print(sel[i] + 1, end=" ")
            exit(0)
        return

    for j in range(2):
        if like[idx][j] == -1:
            continue
        num = like[idx][j]
        if not visit[num]:
            visit[num] = True
            sel[num] = idx
            dfs(idx + 1)
            visit[num] = False


def check():
    for a, b, like in tree:
        frog1 = sel[a]
        frog2 = sel[b]
        if frog[frog1][like] != frog[frog2][like]:
            return False
    return True


N, M = map(int, input().split())
frog = [list(map(int, input().split())) for _ in range(N)]
like = [list(map(int, input().split())) for _ in range(N)]
tree = [list(map(int, input().split())) for _ in range(M)]

# 1-base index to 0-base index
for i in range(N):
    for j in range(2):
        like[i][j] -= 1
    if like[i][0] == like[i][1]:
        like[i][1] = -1
for t in tree:
    for j in range(3):
        t[j] -= 1

sel = [0] * N
visit = [False] * N

ans = "NO"
dfs(0)
print(ans)
