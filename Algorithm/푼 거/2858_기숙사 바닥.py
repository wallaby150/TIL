R, B = map(int, input().split())
a = (R + 4) // 2    # x + y
b = R + B           # x * y

for i in range(1, a):
    if (a - i) * i == b:
        print(max(i, a - i), min(i, a - i))
        break
