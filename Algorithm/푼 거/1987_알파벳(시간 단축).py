import sys
input = sys.stdin.readline.strip()

n, m = map(int, input().split())
grid = [input() for _ in range(n)]

# 방향 벡터 (하, 우, 상, 좌)
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# 방문 여부를 비트마스크로 기록하는 배열
visited = [[0] * m for _ in range(n)]

# 시작점: (0, 0)에서 탐색 시작
stack = [(0, 0, 1, 1 << (ord(grid[0][0]) - 65))]

max_steps = 0

# DFS 반복 탐색
while stack:
    x, y, step_count, bitmask = stack.pop()
    max_steps = max(max_steps, step_count)

    # 모든 알파벳을 방문한 경우 종료
    if max_steps == 26:
        print(26)
        exit()

    # 4방향으로 이동
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            next_bit = 1 << (ord(grid[nx][ny]) - 65)
            # 새로운 알파벳을 방문하는 경우
            if not bitmask & next_bit:
                new_bitmask = bitmask | next_bit
                # 새로운 상태로 방문한 적이 없으면 진행
                if new_bitmask != visited[nx][ny]:
                    visited[nx][ny] = new_bitmask
                    stack.append((nx, ny, step_count + 1, new_bitmask))

# 결과 출력
print(max_steps)
