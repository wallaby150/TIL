import sys
input = lambda : sys.stdin.readline().rstrip()

yd = input()
N = int(input())
names = sorted([input() for i in range(N)])
high_p, high_idx = 0, 0

for i in range(N):
    L = yd.count("L") + names[i].count("L")
    O = yd.count("O") + names[i].count("O")
    V = yd.count("V") + names[i].count("V")
    E = yd.count("E") + names[i].count("E")
    p = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100

    if high_p < p:
        high_p = p
        high_idx = i

print(names[high_idx])