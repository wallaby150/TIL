N = int(input())
arr = [input() for _ in range(N)]
a, b = arr.index('KBS1'), arr.index('KBS2')
b = b+1 if a > b else b

print('1' * a + '4' * a + '1' * b + '4' * (b - 1))