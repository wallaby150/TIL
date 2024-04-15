text = input()
N = len(text) if len(text) <= 9 else 9 + (len(text) - 9) // 2
visited = [0] * (N + 1)
ans = []


def solve(idx):
    if idx == len(text):
        print(*ans)
        exit()

    one = int(text[idx])
    if text[idx] != '0' and not visited[one]:
        visited[one] = 1
        ans.append(text[idx])
        solve(idx + 1)
        ans.pop()
        visited[one] = 0

    two = int(text[idx: idx + 2])
    if idx != len(text) - 1 and text[idx] != '0' and two <= N and not visited[two]:
        visited[two] = 1
        ans.append(text[idx:idx + 2])
        solve(idx + 2)
        ans.pop()
        visited[two] = 0

solve(0)
