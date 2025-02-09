N = int(input())
S = input()

total = 0
num = ""

for char in S:
    if char.isdigit():
        num += char
    else:
        if num:
            total += int(num)
            num = ""

if num:
    total += int(num)

print(total)