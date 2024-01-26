import sys
input = lambda : sys.stdin.readline().rstrip()

T = int(input())

def solve(idx, score):
    global answer

    if idx == N * 2:
        if answer < score:
            print(visited)
        answer = max(score, answer)
        return

    if visited[idx//N][idx % N] == 1:
        solve(idx + 1, score)
        return

    if idx >= N:
        new_idx = idx - N
        tmp = [[idx//N, idx % N]]
        for y, x in ((1, new_idx - 1), (0, new_idx), (1, new_idx + 1)):
            if 0 <= x < N:
                visited[y][x] = 1
                tmp.append([y, x])
        visited[idx//N][idx % N] = 2
        solve(idx + 1, score + nums[1][new_idx])
        for ny, nx in tmp:
            visited[ny][nx] = 0
        solve(idx + 1, score)

    else:
        tmp = [[idx//N, idx % N]]
        for y, x in ((0, idx - 1), (1, idx), (0, idx + 1)):
            if 0 <= x < N:
                visited[y][x] = 1
                tmp.append([y, x])
        visited[idx//N][idx % N] = 2
        solve(idx + 1, score + nums[0][idx])
        for ny, nx in tmp:
            visited[ny][nx] = 0
        solve(idx + 1, score)


for _ in range(T):
    answer = 0

    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(2)]
    visited = [[0] * N for _ in range(2)]
    solve(0, 0)
    print(answer)