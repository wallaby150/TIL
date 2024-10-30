import sys
input = lambda: sys.stdin.readline().rstrip()

txt = input()
l = len(txt)

x, y = 0, 0

for i in range(1, int(l / 2) + 1):
    for j in range(i, l + 1):
        if i * j == l:
            x, y = i, j

for i in range(x):
    for j in range(y):
        print(txt[i + j * x], end='')
