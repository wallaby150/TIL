import sys
from collections import defaultdict
from itertools import chain
input = lambda: sys.stdin.readline().rstrip()

R, C, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(3)]
N, M = 3, 3
cnt = 0


# R연산
def cal_R():
    global M
    # 최장 길이
    max_l = 0
    
    # 바뀌게 될 행들 정보
    changed = []
    for line in grid:
        tmp = defaultdict(int)
        for num in line:
            if num != 0:
                tmp[num] += 1
            
        # 빈도 순으로 정렬
        nums = sorted(list(tmp.items()), key=lambda x: (x[1], x[0]))
        # 최대 길이 갱신
        max_l = min(max(max_l, len(nums)*2), 100)
        changed.append(nums)

    for i in range(N):
        changed_line = list(chain(*changed[i]))[:max_l]
        changed_line += [0] * (max_l - len(changed_line))
        grid[i] = changed_line

    M = max_l
    return


def cal_L():
    global N
    max_l = 0

    changed = []
    for x in range(M):
        tmp = defaultdict(int)
        for y in range(N):
            num = grid[y][x]
            if num != 0:
                tmp[num] += 1

        # 빈도 순으로 정렬
        nums = sorted(list(tmp.items()), key=lambda x: (x[1], x[0]))
        # 최대 길이 갱신
        max_l = min(max(max_l, len(nums) * 2), 100)
        changed.append(nums)

    N = max_l
    while len(grid) < max_l:
        grid.append([0] * M)

    for x in range(M):
        changed_line = list(chain(*changed[x]))[:max_l]
        changed_line += [0] * (max_l - len(changed_line))
        for y in range(N):
            grid[y][x] = changed_line[y]
    return


while True:
    if N - 1 >= R-1 and M - 1 >= C-1:
        if K == grid[R-1][C-1]:
            print(cnt)
            break

    cnt += 1
    if cnt > 100:
        break
    if M <= N:
        cal_R()
    else:
        cal_L()

else:
    print(-1)