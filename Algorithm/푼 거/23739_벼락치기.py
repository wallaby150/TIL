import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
time = 30
cnt = 0

for _ in range(N):
    need = int(input())
    if time >= need:
        cnt += 1
        time -= need
    else:
        if time >= need / 2:
            cnt += 1
        time = 0

    if not time:
        time = 30

print(cnt)