import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
words = []

# 입력 단계에서 길이 조건에 맞는 단어만 리스트에 추가
for _ in range(N):
    word = input()
    if len(word) >= M:
        words.append(word)

# Counter를 통해 빈도수 계산
counter = Counter(words)

# 빈도수, 단어 길이, 알파벳 순으로 정렬
ans = sorted(counter, key=lambda x: (-counter[x], -len(x), x))

# 최종 결과 출력
print('\n'.join(ans))
