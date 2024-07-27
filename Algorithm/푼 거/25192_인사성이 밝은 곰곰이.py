import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
ans = 0
log = set()

for _ in range(N):
    word = input()
    if word == "ENTER":
        log.clear()

    else:
        if word not in log:
            ans += 1
            log.add(word)

print(ans)
