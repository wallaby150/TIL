import sys
input = lambda: sys.stdin.readline().rstrip()

N, atk = map(int, input().split())
rooms = [0] * N
for i in range(N):
    rooms[i] = list(map(int, input().split()))


def adventure(hp):
    now_atk = atk
    now_hp = hp

    for room in rooms:
        t, a, h = room
        # 몬스터 만남
        if t == 1:
            cnt = h // now_atk if not h % now_atk else h // now_atk + 1
            now_hp -= a * (cnt - 1)
            if now_hp <= 0:
                return False
        # 포션 섭취
        elif t == 2:
            now_atk += a
            now_hp = min(now_hp + h, hp)

    return True


def solve():
    l, r = 0, 10 ** 18
    ans = 0

    while l <= r:
        m = (l + r) // 2

        if adventure(m):
            r = m - 1
            ans = m
        else:
            l = m + 1

    return ans


print(solve())
