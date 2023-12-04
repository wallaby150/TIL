import sys
input = lambda: sys.stdin.readline().rstrip()

# 가로 N, 세로 M
N, M, K = map(int, input().split())
nums = list(list(map(int, input().split())) for _ in range(N))
visited = list([False] * M for _ in range(N))
answer = -10000 * 101

def solve(ny, nx, cnt, now_sum):
    global answer

    if now_sum + (K - cnt + 1) * 10000 <= answer:
        return

    if cnt == K:
        answer = max(now_sum, answer)
        return

    for y in range(ny, N):
        for x in range(M):
            if y == ny and x < nx:
                continue

            # 얘의 4분면이 가능한지 확인
            for ty, tx in ((y-1, x), (y+1, x), (y, x+1), (y, x-1)):
                if 0 <= ty < N and 0 <= tx < M:
                    if visited[ty][tx]:
                        break
            else:
                # 가능하다면
                visited[y][x] = True
                solve(y, x + 1, cnt + 1, now_sum + nums[y][x])
                visited[y][x] = False

solve(0, 0, 0, 0)
print(answer)