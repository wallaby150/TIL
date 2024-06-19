import sys
input = lambda: sys.stdin.readline().rstrip()


def solve(dots):
    dist = []
    for i in range(4):
        for j in range(i+1, 4):
            x1, y1 = dots[i]
            x2, y2 = dots[j]
            dist.append(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)

    dist.sort()
    # 네 변의 길이가 같고, 두 대각선의 길이가 같은지 확인
    if dist[0] == dist[1] == dist[2] == dist[3] and dist[4] == dist[5]:
        return 1
    else:
        return 0


T = int(input())
for _ in range(T):
    now = [list(map(int, input().split())) for _ in range(4)]
    print(solve(now))
