input()
a = [0] * 1001
for i in map(int, input().split()):
    a[i] = max(a[:i]) + i
print(max(a))
