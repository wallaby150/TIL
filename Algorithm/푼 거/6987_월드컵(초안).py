def dfs(idx, remains, k):
    if k == 6:
        return not sum(remains) and solve(idx + 1)

    win, draw, lose = remains
    if idx != k and result[idx][k] == -3:
        if win:
            result[idx][k], result[k][idx] = 1, -1
            if dfs(idx, [win-1, draw, lose], k+1):
                return True
            result[idx][k], result[k][idx] = -3, -3

        if draw:
            result[idx][k], result[k][idx] = 0, 0
            if dfs(idx, [win, draw-1, lose], k+1):
                return True
            result[idx][k], result[k][idx] = -3, -3

        if lose:
            result[idx][k], result[k][idx] = -1, 1
            if dfs(idx, [win, draw, lose-1], k+1):
                return True
            result[idx][k], result[k][idx] = -3, -3
    else:
        return dfs(idx, remains, k+1)

    return False


def solve(idx):
    if idx == 6:
        return True

    todos = nums[idx*3:idx*3+3]
    now = [result[idx].count(i) for i in [1, 0, -1]]

    if any(todos[i] < now[i] for i in range(3)):
        return False

    remains = [todos[j] - now[j] for j in range(3)]
    return dfs(idx, remains, 0)


for _ in range(4):
    result = [[-3] * 6 for _ in range(6)]
    nums = list(map(int, input().split()))
    print(1 if solve(0) else 0, end=' ')
