GPA = ['A+'] * 5 + ['A0'] * 10 + ['B+'] * 15 + ['B0'] * 5 + ['C+'] * 10 + ['C0'] * 3 + ['F'] * 2
scores = list(map(int, input().split()))
hong = int(input())
rank = scores.index(hong)
print(GPA[scores.index(hong)])