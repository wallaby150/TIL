import sys
input = lambda : sys.stdin.readline().rstrip()

N, Q = map(int, input().split())
occupied = set()

for _ in range(Q):
    num = int(input())
    route = num
    first_land = 0  # 가장 처음 만나는 땅
    while route > 0:
        if route in occupied:
            first_land = route
        route //= 2

    if first_land == 0:
        occupied.add(num)
    print(first_land)
