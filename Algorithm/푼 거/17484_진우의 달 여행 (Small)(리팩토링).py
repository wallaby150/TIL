import sys
input = sys.stdin.readline


def solve():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 이전 행의 dp 값을 저장할 리스트
    prev_dp = [[float('inf')] * M for _ in range(3)]

    # 첫 번째 행 초기화
    for x in range(M):
        for d in range(3):
            prev_dp[d][x] = grid[0][x]

    directions = [-1, 0, 1]

    for y in range(1, N):
        # 현재 행의 dp 값을 저장할 리스트
        curr_dp = [[float('inf')] * M for _ in range(3)]

        for x in range(M):
            for prev_d in range(3):
                for curr_d in range(3):
                    if prev_d == curr_d:
                        continue
                    nx = x + directions[curr_d]
                    if 0 <= nx < M:
                        curr_dp[curr_d][x] = min(curr_dp[curr_d][x], prev_dp[prev_d][nx] + grid[y][x])

        # 현재 dp 값을 이전 dp 값으로 업데이트
        prev_dp = curr_dp

    # 마지막 행에서 최소값 찾기
    return min(min(prev_dp[d][x] for d in range(3)) for x in range(M))


print(solve())

'''
# 개선사항
1. 메모리 사용 최적화: dp 배열을 2차원 배열로 줄였습니다. 각 행에 대해 필요한 메모리만 사용하여 공간 복잡도를 줄였습니다.
2. 이전 행만 유지: prev_dp와 curr_dp 두 개의 배열만 사용하여 현재 행과 이전 행의 정보를 유지합니다. 이는 메모리 사용을 크게 줄이는 동시에 성능을 향상시킵니다.
3. 불필요한 계산 제거: 불필요한 범위 체크를 제거하고, 필요한 경우에만 방향 전환을 고려하여 효율성을 높였습니다.
'''