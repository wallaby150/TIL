import sys
input = lambda : sys.stdin.readline().rstrip()

s = input()
t = input()

fs = s
ft = t

while len(fs) != len(ft):
    if len(fs) > len(ft):
        ft += t
    else:
        fs += s

if fs == ft:
    print(1)
else:
    print(0)