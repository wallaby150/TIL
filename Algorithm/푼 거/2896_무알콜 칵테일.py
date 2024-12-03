A, B, C = map(int, input().split())
I, J, K = map(int, input().split())

ratio = min(A/I, B/J, C/K)
drinks = ratio * I, ratio * J, ratio * K

print(A - drinks[0], B - drinks[1], C - drinks[2])