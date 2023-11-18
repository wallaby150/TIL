import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
H = list(map(int, input().split()))
arrows = [0] * 1000001
count = 0

for height in H:
    if arrows[height]:
        arrows[height] -= 1
        arrows[height - 1] += 1

    else:
        arrows[height - 1] += 1
        count += 1

print(count)