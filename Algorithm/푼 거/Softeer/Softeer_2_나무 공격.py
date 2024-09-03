import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
row_count = [0]

for _ in range(N):
    cnt = input().count('1')
    row_count.append(cnt)

for _ in range(2):
    s, e = map(int, input().split())
    for row in range(s, e+1):
        if row_count[row]:
            row_count[row] -= 1

print(sum(row_count))
