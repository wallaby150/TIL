text = ''
N = int(input())
for _ in range(N + N - 1):
    text += input().replace('/', '//')
print(eval(text))