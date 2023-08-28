import sys
input = lambda : sys.stdin.readline().rstrip()

a = []
for _ in range(int(input())):
    a.append(int(input()))
a.sort(reverse=True)

count = 0
for i in range(len(a)):
    if a[i] - i > 0:
        count += a[i] - i
    else:
        break

print(count)