a, b, c = map(int, input().split())
if c % 2:
    print(a ^ b)
else:
    print((a ^ b) ^ b)
