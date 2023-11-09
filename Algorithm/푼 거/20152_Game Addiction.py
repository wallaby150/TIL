home, pc = map(int, input().split())

b = abs(home - pc) + 1
road = list([0] * b for _ in range(b))

for i in range(b):
    road[0][i] = 1

for i in range(1, b):
    for j in range(i, b):
        road[i][j] = road[i-1][j] + road[i][j-1]

print(road[-1][-1])