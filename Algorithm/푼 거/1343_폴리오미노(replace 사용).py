import sys
input = lambda : sys.stdin.readline().rstrip()

t = input()
t = t.replace("XXXX", "AAAA")
t = t.replace("XX", "BB")

for char in t:
    if char == 'X':
        print(-1)
        break
else:
    print(t)