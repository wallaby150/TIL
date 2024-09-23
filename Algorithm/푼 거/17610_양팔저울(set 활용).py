import sys
input = lambda: sys.stdin.readline().rstrip()

K = int(input())
nums = list(map(int, input().split()))
possibles = set()

for num in nums:
    tmp = []
    for p in possibles:
        tmp.append(num + p)
        tmp.append(abs(num - p))
    possibles.add(num)
    possibles.update(tmp)

possibles.discard(0)
print(max(possibles)-len(possibles))
