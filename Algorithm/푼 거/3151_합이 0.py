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


# print(score_dict)
# print(scores)

l = 0
while scores[l] <= 0 and l <= N-2:
    for r in range(N-1, l, -1):
        # 왼쪽으로 많이 넘어가면
        if scores[r] < 0:
            break
        ln, rn = scores[l], scores[r]
        gap = scores[l] + scores[r]
        if -gap == scores[l] and -gap == scores[r]:
            if -gap in score_dict and score_dict[-gap] >= 3:
                answer += score_dict[-gap] - 2
        elif -gap == scores[l] or -gap == scores[r]:
            if -gap in score_dict and score_dict[-gap] >= 2:
                answer += score_dict[-gap] - 1
        else:
            if -gap in score_dict:
                answer += score_dict[-gap]
    l += 1


print(answer // 2)