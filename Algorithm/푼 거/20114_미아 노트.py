import sys
input = lambda: sys.stdin.readline().rstrip()

# 원래 문자열 길이, 세로로 번진 글자의 개수, 가로로 번진 글자의 개수
N, H, W = map(int, input().split())
text = ['?'] * N


for _ in range(H):
    now = input()

    for i in range(0, N * W, W):
        for j in range(W):
            if now[i+j] != '?' and text[i//W] == '?':
                text[i//W] = now[i+j]

print(''.join(text))