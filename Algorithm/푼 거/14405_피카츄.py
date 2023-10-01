import sys
input = lambda : sys.stdin.readline().rstrip()

s = input()
tmp = ''
for char in s:
    tmp += char
    if tmp in ["pi", "ka", "chu"]:
        tmp = ''

if tmp == '':
    print("YES")
else:
    print("NO")