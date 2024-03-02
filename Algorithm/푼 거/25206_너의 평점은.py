import sys
input = lambda : sys.stdin.readline().rstrip()

R, S = 0, 0
rates = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

for i in range(20):
    sub, score, grade = input().split()
    if grade == "P":
        continue
    R += float(score) * rates[grade]
    S += float(score)

print(R / S)