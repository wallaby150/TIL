import sys
input = lambda : sys.stdin.readline().rstrip()

S = input()
zero_count = 0
one_count = 0
zero_switch = False
one_switch = False

for char in S:
    if zero_switch == False and char == '0':
        zero_switch = True
        zero_count += 1

    elif zero_switch == True and char == '1':
        zero_switch = False

    if one_switch == False and char == '1':
        one_switch = True
        one_count += 1

    elif one_switch == True and char == '0':
        one_switch = False

print(zero_count, one_count)
print(min(zero_count, one_count))