def DFS():
    N, K = map(int, input().split())

    # 0은 Left, 1은 Right
    grid = [input(), input()]
    visited = [[0] * N for _ in range(2)]

    q = [[0, 0, 0]]

    while q:
        idx, line, time = q.pop()
        for ti, tl in [(idx+1, line),
                       (idx-1, line),
                       (idx+K, line^1)]:
            if ti >= N:
                return 1
            # 시간보다 앞, 갈 수 있어야 함, 간 적 없음
            if time < ti and grid[tl][ti] == '1' and not visited[tl][ti]:
                q.append([ti, tl, time + 1])
                visited[tl][ti] = 1
    return 0


print(DFS())
