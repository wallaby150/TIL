import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
total_scores = [0 for _ in range(N)]


def sorting(n, scores):
    sorted_scores = sorted(scores, reverse=True)
    score = 3001
    i = 0
    score_dict = {}

    for idx in range(n):
        now = sorted_scores[idx]
        if now != score:
            score_dict[now] = idx+1
            score = now

    for idx in range(n):
        j = scores[idx]
        total_scores[idx] = total_scores[idx]+j
        if idx == n - 1:
            print(score_dict[j])
        else:
            print(score_dict[j], end=" ")


for _ in range(3):
    scores_list = list(map(int, input().split()))
    sorting(N, scores_list)

sorting(N, total_scores)