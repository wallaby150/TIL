import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
# 격자 초기화: 위아래에 0으로 채워진 행 추가
grid = [[0] * M] + [list(map(int, input().split())) for _ in range(N)] + [[0] * M]
# DP 배열 초기화: 각 위치에서 3가지 방향(-1, 0, 1)에 대한 최소 연료 소비량 저장
dp = [[[0] * 3 for _ in range(M)]] + [[[float('inf')] * 3 for _ in range(M)] for _ in range(N + 1)]
# 방향 정의: 왼쪽 대각선, 수직, 오른쪽 대각선
directions = [-1, 0, 1]

# DP 계산
for y in range(1, N + 2):
    for x in range(M):
        for prev_d in range(3):  # 이전 방향
            for curr_d in range(3):  # 현재 방향
                if prev_d == curr_d:
                    continue  # 같은 방향으로 연속 이동 불가

                nx = x + directions[curr_d]
                if 0 <= nx < M:
                    dp[y][nx][curr_d] = min(dp[y][nx][curr_d], dp[y - 1][x][prev_d] + grid[y][nx])

# 마지막 행에서 최소값 찾기
print(min(min(dp[-1][x]) for x in range(M)))
