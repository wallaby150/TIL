def char_to_number(c):
    if c.islower():
        return ord(c) - 70  # 'a' -> 27, ..., 'z' -> 52
    elif c.isupper():
        return ord(c) - 64  # 'A' -> 1, ..., 'Z' -> 26
    else:
        return 0            # 공백 -> 0

def is_valid_decryption(n, lis, s):
    if len(s) > n:
        return "n"

    number = [char_to_number(c) for c in s]

    if sorted(lis) == sorted(number):
        return "y"
    else:
        return "n"

n = int(input())
lis = list(map(int, input().split()))
s = input()

print(is_valid_decryption(n, lis, s))
