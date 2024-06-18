import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())


def solve(dots):
    dist = []
    x1, x2 = dots[0]
    for i in range(1, 4):
        y1, y2 = dots[i]
        tmp = ((x1 - y1) ** 2 + (x2 - y2) ** 2) ** 0.5
        dist.append(tmp)

    for j in range(2):
        for k in range(j+1, 3):
            if dist[j] == dist[k]:
                nums = {0, 1, 2, 3} - {j , k}

                for num in nums:
                    rest = [1, 2, 3]
                    rest.remove(num+1)

                    if dist[num] == ((dots[rest[0]][0] - dots[rest[1]][0]) ** 2 + (dots[rest[0]][1] - dots[rest[1]][1]) ** 2) ** 0.5:
                        return 1

        return 0




for _ in range(T):
    now = [list(map(int, input().split())) for _ in range(4)]
    print(solve(now))
