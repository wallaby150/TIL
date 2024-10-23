import sys
input = lambda: sys.stdin.readline().rstrip('\n')

while True:
    text = input()

    if not text:
        break

    l, u, d, s = 0, 0, 0, 0
    for char in text:
        if char.islower():
            l += 1
        elif char.isupper():
            u += 1
        elif char.isdigit():
            d += 1
        elif char.isspace():
            s += 1

    print(l, u, d, s)
