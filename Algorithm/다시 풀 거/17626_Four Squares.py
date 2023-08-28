n = int(input())

def solve(num):
    base = [0]
    root = num ** 0.5
    if root == int(root):
        return 1

    for i in range(1, int(root) + 1):
        base.append(i ** 2)

    for j in base:
        if num-j in base:
            return 2

    for i in base:
        for j in base:
            if num-i-j in base:
                return 3

    return 4

print(solve(n))