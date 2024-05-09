import sys
input = lambda: sys.stdin.readline().rstrip()

keys = {'z': (0, 0), 'x': (0, 1), 'c': (0, 2), 'v': (0, 3), 'b': (0, 4), 'n': (0, 5), 'm': (0, 6),
        'a': (1, 0), 's': (1, 1), 'd': (1, 2), 'f': (1, 3), 'g': (1, 4), 'h': (1, 5), 'j': (1, 6), 'k': (1, 7), 'l': (1, 8),
        'q': (2, 0), 'w': (2, 1), 'e': (2, 2), 'r': (2, 3), 't': (2, 4), 'y': (2, 5), 'u': (2, 6), 'i': (2, 7), 'o': (2, 8), 'p': (2, 9)}

l, r = input().split()
l, r = keys[l], keys[r]
c = ('q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v')
time = 0

for char in input():
    ty, tx = keys[char]
    if char in c:
        time += abs(l[0] - ty) + abs(l[1] - tx) + 1
        l = keys[char]
    else:
        time += abs(r[0] - ty) + abs(r[1] - tx) + 1
        r = keys[char]

print(time)
