N = int(input())
A = list(map(int, input().split()))
sorted_A = sorted(A)
B = dict()

for num in A:
    if num not in B.keys():
        B[num] = sorted_A.index(num)
    else:
        B[num] = B[num] + 1
    print(B[num], end=" ")
