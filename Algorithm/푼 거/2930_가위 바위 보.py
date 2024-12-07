import sys
input = lambda: sys.stdin.readline().rstrip()


def game(a, b):
    if a == b:
        return 1
    if (a == 'R' and b == 'S') or (a == 'S' and b == 'P') or (a == 'P' and b == 'R'):
        return 2
    return 0


R = int(input())
sanggeun = input()
N = int(input())
friends = [input() for _ in range(N)]

actual_score = 0
for i in range(R):
    for friend in friends:
        actual_score += game(sanggeun[i], friend[i])

max_score = 0
for i in range(R):
    round_scores = [0, 0, 0]  # R, S, P
    for friend in friends:
        round_scores[0] += game('R', friend[i])
        round_scores[1] += game('S', friend[i])
        round_scores[2] += game('P', friend[i])
    max_score += max(round_scores)

print(actual_score)
print(max_score)