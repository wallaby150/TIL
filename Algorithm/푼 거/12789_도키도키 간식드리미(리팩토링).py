import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
line = list(map(int, input().split()))
stack = []
target = 1

for num in line:
    if num == target:
        target += 1
    else:
        stack.append(num)

    while stack and stack[-1] == target:
        stack.pop()
        target += 1

if not stack:
    print("Nice")
else:
    print("Sad")