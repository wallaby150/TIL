import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
count = 0

for _ in range(N):
    word = input()
    stack = []

    for char in word:
        # 스택이 비어있으면
        if not stack:
            stack.append(char)
        else:
            if char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)

    else:
        if not stack:
            count += 1

print(count)