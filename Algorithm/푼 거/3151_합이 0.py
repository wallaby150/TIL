import sys
from collections import defaultdict
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
scores = list(map(int, input().split()))
scores.sort()
answer = 0
score_dict = defaultdict(int)
for score in scores:
    score_dict[score] += 1

for i in range(N-2):
    l, r = i + 1, N - 1
    t = -scores[i]

    while l < r:
        tmp = scores[l] + scores[r]
        if tmp < t:
            l += 1
        elif tmp > t:
            r -= 1
        else:
            if scores[l] == scores[r]:
                answer += r - l
            else:
                answer += score_dict[scores[r]]
            l += 1

print(answer)