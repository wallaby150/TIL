A, B = input().split()

for i, a in enumerate(A):
    if a in B:
        a_idx = i
        b_idx = B.index(a)
        break

for i in range(len(B)):
    if i == b_idx:
        print(A)
    else:
        print('.' * a_idx + B[i] + '.' * (len(A) - a_idx - 1))
