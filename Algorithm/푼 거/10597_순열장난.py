text = input()
N = min(len(text), 9) + max(len(text) - 9, 0) // 2
visited = [0] * (N + 1)

def solve(idx, now):
    if idx == len(text):
        return now

    one = int(text[idx])
    if not visited[one] and one != 0:
        visited[one] = 1
        tmp = now + [one]
        a = solve(idx + 1, tmp)
        if a:
            return a
        visited[one] = 0

    if idx != len(text) - 1:
        two = int(text[idx:idx+2])

        if two <= N and not visited[two]:
            visited[two] = 1
            tmp2 = now + [two]
            b = solve(idx + 2, tmp2)
            if b:
                return b
            visited[two] = 0
        return False

ans = solve(0, [])
print(*ans)
