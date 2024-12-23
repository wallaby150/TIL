a, b = input().split()

if len(a) < len(b):
    a, b = b, a

l = len(a)
b = b.zfill(l)
result = ''.join(str(int(a[i]) + int(b[i])) for i in range(l))
print(result)
