a, b = input().split()

if len(a) < len(b):
    a, b = b, a

b = b.zfill(len(a))
result = ''.join(str(int(x) + int(y)) for x, y in zip(a, b))
print(result)
