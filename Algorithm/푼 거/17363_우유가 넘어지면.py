dict = {'.': '.', 'O': 'O', '-': '|', '|': '-', '\\': '/', '/': '\\', '^': '<', '<': 'v', 'v': '>', '>': '^'}

N, M = map(int, input().split())
rotated = [[''] * N for _ in range(M)]

for i in range(N):
    line = input()
    for j in range(M):
        rotated[M - j - 1][i] = dict[line[j]]

for row in rotated:
    print(''.join(row))
