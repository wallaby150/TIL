import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
text = input()
nums = list(int(input()) for _ in range(N))
stack = []

for char in text:
    if char not in '+-*/':
        stack.append(nums[ord(char) - 65])
    else:
        b, a = stack.pop(), stack.pop()
        if char == '+':
            c = a + b
        elif char == '-':
            c = a - b
        elif char == '*':
            c = a * b
        else:
            c = a / b
        stack.append(c)

print('%.2f' %stack[0])