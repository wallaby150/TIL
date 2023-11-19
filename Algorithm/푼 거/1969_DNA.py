import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
dna_list = list(input() for _ in range(N))
answer = ''
count = 0

for idx in range(M):
    # A, C, G, T
    tmp = [0, 0, 0, 0]

    for dna in dna_list:
        if dna[idx] == 'A':
            tmp[0] += 1
        elif dna[idx] == 'C':
            tmp[1] += 1
        elif dna[idx] == 'G':
            tmp[2] += 1
        else:
            tmp[3] += 1

    f = max(tmp)
    answer += 'ACGT'[tmp.index(f)]
    count += N - f

print(answer)
print(count)