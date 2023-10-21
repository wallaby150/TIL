import sys
input = lambda : sys.stdin.readline().rstrip()
from pprint import pprint

# 세로, 가로
R, S = map(int, input().split())
pic = list(list(map(str, input())) for _ in range(R))
lands = set()
min_height = R
star = []

# x좌표 별로 제일 높은 땅과 가장 낮은 유성 확인
for x in range(S):
    low_star = -R
    high_ground = R
    # 가장 낮은 유성 발견 여부
    flag = False

    for y in range(R-1, -1, -1):
        if pic[y][x] == 'X':
            # 가장 낮은 유성 발견
            if not flag:
                flag = True
                low_star = y
            # 유성 위치 저장
            star.append((y, x))

        # 가장 높은 땅 저장
        elif pic[y][x] == '#':
            high_ground = y

    min_height = min(min_height, high_ground - low_star - 1)

for sy, sx in sorted(star, reverse=True):
    pic[sy][sx] = '.'
    pic[sy+min_height][sx] = 'X'


for line in pic:
    print(''.join(line))