import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
M = int(input())
vip = set()
for _ in range(M):
    vip.add(int(input()))

count = 0

def solve(idx, last):
    global count
    if idx == N:
        count += 1
        return

    if idx in vip:
        solve(idx+1, idx)

    else:
        for i in range(idx-1, idx+2):
            if i in vip:
                continue

            elif i != last and i != 0:
                solve(idx+1, i)

solve(1, -1)
print(count)