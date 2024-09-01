import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    N = int(input())
    parents = [i for i in range(N + 1)]
    road = set()

    for _ in range(N-1):
        a, b = map(int, input().split())
        parents[b] = a

    c, d = map(int, input().split())

    first = c
    road.add(c)
    while first != parents[first]:
        first = parents[first]
        road.add(first)

    second = d
    while second != parents[second]:
        if parents[second] in road:
            break
        second = parents[second]
    print(parents[second])
