N = int(input())
N %= 8
print((10 - N) % 8 if N > 5 or N == 0 else N)
