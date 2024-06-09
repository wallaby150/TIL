import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
K += 1

B = {0: 0}
L = [tuple(map(int, input().split())) for _ in range(N)]
L.sort(reverse=True)

for w, v in L:
    T = {}
    for V, W in B.items():
        if B.get(nv := v + V, K) > (nw := w + W):
            T[nv] = nw
    B.update(T)

print(max(B.keys()))