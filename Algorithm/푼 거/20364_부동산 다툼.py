import sys
input = lambda : sys.stdin.readline().rstrip()

# 땅의 갯수 N, 오리의 수 K
N, Q = map(int, input().split())
land = [False] * (N+1)

for _ in range(Q):
    num = int(input())
    tmp = []
    way = num

    while way:
        tmp.append(way)
        way //= 2

    for route in sorted(tmp):
        if land[route]:
            print(route)
            break
    else:
        land[num] = True
        print(0)