def dfs(depth):
    global result
    if depth == 15:
        if sum(sum(r) for r in result) == 0:
            return True
        return False

    team1, team2 = game[depth]
    for x, y in ((0, 2), (1, 1), (2, 0)):
        if result[team1][x] > 0 and result[team2][y] > 0:
            result[team1][x] -= 1
            result[team2][y] -= 1
            if dfs(depth + 1):
                return True
            result[team1][x] += 1
            result[team2][y] += 1
    return False


game = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
        (1, 2), (1, 3), (1, 4), (1, 5),
        (2, 3), (2, 4), (2, 5),
        (3, 4), (3, 5),
        (4, 5)]

for _ in range(4):
    input_data = list(map(int, input().split()))
    result = [input_data[i:i + 3] for i in range(0, 16, 3)]
    print(1 if dfs(0) else 0, end=' ')
print()