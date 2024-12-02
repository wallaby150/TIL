def solve(text):
    ans = 1
    pre = None

    for char in text:
        if char == 'c':
            choices = 26
        elif char == 'd':
            choices = 10
        else:
            continue

        if char == pre:
            choices -= 1

        ans *= choices
        pre = char

    return ans


sign = input()
print(solve(sign))
