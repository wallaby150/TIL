N, M = map(int, input().split())
x = ""
for _ in range(N):
    for char in input():
        x += char * 2

y = ""
for _ in range(N):
    y += input()

print('Eyfa' if x == y else 'Not Eyfa')