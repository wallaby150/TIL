a, b = input().split()
if len(a) < len(b):
    a, b = b, a

d = len(a) - len(b)
ans = a[:d]
a = a[d:]

for i in range(len(b)):
    l, r = a[i], b[i]
    ans += str(int(l) + int(r))

print(ans)