import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
t = input()
l = len(t)
olds = list(input() for _ in range(N))
cnt = 0


def check(s):
    term = 1
    while True:
        idx = s
        for j in range(l - 1):
            idx += term
            if idx >= len(old):
                return False
            else:
                if old[idx] != t[j+1]:
                    break
        else:
            return True
        term += 1


for old in olds:
    for i in range(len(old)):
        char = old[i]
        if char == t[0]:
            if check(i):
                cnt += 1
                break

print(cnt)