import sys

input = lambda: sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())
directions = {0: (-1, 0),
              1: (-1, 1),
              2: (0, 1),
              3: (1, 1),
              4: (1, 0),
              5: (1, -1),
              6: (0, -1),
              7: (-1, -1)}
balls = {}

for _ in range(M):
    y, x, m, s, d = map(int, input().split())
    balls[(y - 1, x - 1)].append((m, s, d))


def split(next_balls, multiple_balls):
    for (y, x) in multiple_balls:
        # 질량의 합, 속력의 합, 방향 리스트
        total_mass, total_speed, directions_list = 0, 0, []
        for mass, speed, direction in next_balls[(y, x)]:
            total_mass += mass
            total_speed += speed
            directions_list.append(direction)

        # 질량이 0이면 소멸
        new_mass = total_mass // 5
        if new_mass == 0:
            del next_balls[(y, x)]
            continue

        new_speed = total_speed // len(directions_list)
        if all(d % 2 == 0 for d in directions_list) or all(d % 2 == 1 for d in directions_list):
            new_directions = [0, 2, 4, 6]
        else:
            new_directions = [1, 3, 5, 7]


    return next_balls


def move(current_balls):
    next_balls = {}
    multiple_balls = set()
    for (y, x), ball_list in current_balls.items():
        # 질량, 속력, 방향
        for mass, speed, direction in ball_list:
            ty = (y + directions[direction][0] * speed) % N
            tx = (x + directions[direction][1] * speed) % N

            if (ty, tx) in next_balls:
                next_balls[(ty, tx)].append((mass, speed, direction))
                multiple_balls.add((ty, tx))
            else:
                next_balls[(ty, tx)] = [(mass, speed, direction)]

    # 중복되는 위치에 대한 처리
    if multiple_balls:
        next_balls = split(next_balls, multiple_balls)

    return next_balls


while K:
    K -= 1
    balls = move(balls)

total_mass = sum(mass for ball_list in balls.values() for mass, _, _ in ball_list)
print(total_mass)
