N = int(input())
connects = set()

for _ in range(N):
    a, b = map(int, input().split())
    connects.add((min(a, b), max(a, b)))

fox_sign = {(1, 3), (1, 4), (3, 4)}

if connects == fox_sign:
    print("Wa-pa-pa-pa-pa-pa-pow!")
else:
    print("Woof-meow-tweet-squeek")