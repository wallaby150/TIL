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
    balls[(y-1, x-1)] = [(m, s, d)]


def split(next, doubles):
    for (y, x) in doubles:
        # 질량의 합, 속력의 합, 방향의 합
        hm, hs, hd = 0, 0, []
        for nm, ns, nd in next[(y, x)]:
            hm += nm
            hs += ns
            hd.append(nd)

        sm, ss = hm // 5, hs // len(hd)
        # 질량이 0이면 소멸
        if sm == 0:
            del next[(y, x)]
            continue
        # 방향이 모두 홀수거나 짝수면
        if all(d % 2 == 0 for d in hd) or all(d % 2 == 1 for d in hd):
            way = [0, 2, 4, 6]
        else:
            way = [1, 3, 5, 7]
        next[(y, x)] = [(sm, ss, w) for w in way]
    return next


def move(now):
    next = {}
    doubles = set()
    for (ny, nx), ball_list in now.items():
        # 질량, 속력, 방향
        for nm, ns, nd in ball_list:
            ty = (ny + directions[nd][0] * ns) % N
            tx = (nx + directions[nd][1] * ns) % N

            # 이미 같은 자리에 파이어볼이 있다면
            if (ty, tx) in next:
                next[(ty, tx)].append((nm, ns, nd))
                doubles.add((ty, tx))
            else:
                next[(ty, tx)] = [(nm, ns, nd)]

    # 중복되는 게 있다면
    if doubles:
        next = split(next, doubles)
    return next


while K:
    K -= 1
    balls = move(balls)

ans = 0
for ball_list in balls.values():
    for m, s, d in ball_list:
        ans += m
print(ans)