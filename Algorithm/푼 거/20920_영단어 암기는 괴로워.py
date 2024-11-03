import sys, heapq
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
words = defaultdict(int)
hq = []

# 입력 받는 부분
for _ in range(N):
    word = input()
    if len(word) < M:
        continue
    words[word] += 1

# 키는 word, 밸류는 횟수
for k, v in words.items():
    heapq.heappush(hq, (-v, -len(k), k))

while hq:
    print(heapq.heappop(hq)[2])