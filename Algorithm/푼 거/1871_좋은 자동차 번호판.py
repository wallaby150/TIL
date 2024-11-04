for _ in range(int(input())):
    a, b = input().split('-')
    left = 0

    for i in range(3):
        char = a[i]
        left += 26 ** (2-i) * (ord(char) - 65)

    if abs(left - int(b)) <= 100:
        print("nice")
    else:
        print("not nice")