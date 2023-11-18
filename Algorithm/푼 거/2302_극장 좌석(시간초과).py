import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
M = int(input())
vip = set()
take = [0] * (N + 1)
take[0] = 1
for _ in range(M):
    tmp = int(input())
    vip.add(tmp)
    take[tmp] = 1

count = 0

def solve(idx):
    global count
    if idx == N:
        count += 1
        return

    if idx in vip:
        solve(idx+1)

    else:
        for i in range(idx-1, idx+2):
            if take[i] == 0:
                take[i] = 1
                solve(idx+1)
                take[i] = 0

solve(1)
print(count)