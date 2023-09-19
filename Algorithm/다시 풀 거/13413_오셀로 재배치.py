import sys
input = lambda : sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    N = int(input())
    now = input()
    target = input()
    diff = {"W" : 0, "B" : 0}

    for i in range(N):
        if now[i] != target[i]:
            diff[now[i]] += 1

    print(max(diff["W"], diff["B"]))