import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

total_nines = 0
row_count = [0] * N
col_count = [0] * M

for i in range(N):
    for j in range(M):
        count = str(board[i][j]).count('9')
        row_count[i] += count
        col_count[j] += count
        total_nines += count

max_remove = max(max(row_count), max(col_count))

print(total_nines - max_remove)
