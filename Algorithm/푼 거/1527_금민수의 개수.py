import sys
input = lambda: sys.stdin.readline().rstrip()

A, B = input().split()
len_a, len_b = len(A), len(B)
A, B = int(A), int(B)
ans = 0


def backtracking(now, l):
    global ans
    if len(now) == l:
        if A <= int(''.join(map(str, now))) <= B:
            ans += 1
        return

    for num in [4, 7]:
        now.append(num)
        backtracking(now, l)
        now.pop()


for i in range(len_a, len_b + 1):
    backtracking([], i)

print(ans)