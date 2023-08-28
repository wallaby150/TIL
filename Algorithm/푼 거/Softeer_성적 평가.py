import sys
sys.stdin = open("성적 평가.txt")
input = sys.stdin.readline

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
            i = idx
            score = now
        # else:
        #     # 전에 놈이랑 등수가 같으면
        #     score_dict[now] = i

    for idx in range(n):
        j = scores[idx]
        total_scores[idx] = total_scores[idx]+j
        print(score_dict[j], end=" ")
    else:
        print()


for _ in range(3):
    scores_list = list(map(int, input().split()))
    sorting(N, scores_list)

sorting(N, total_scores)

# print(" ".join(map(str, total_scores)))