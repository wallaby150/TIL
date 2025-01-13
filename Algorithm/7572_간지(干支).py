a = 'ABCDEFGHIJKL'
b = '0123456789'
i = int(input()) - 1984
print(a[i % 12] + b[i % 10])
