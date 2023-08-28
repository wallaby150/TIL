import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
total = [[0] * 9 for _ in range(5)]

# 각 학생마다
for student in data:
    # 그 학생의 학년에
    for i in range(5):
        total[i][student[i]-1] += 1


max_student = 0
max_temp = 0

# 각 학생마다
for student_num in range(N):
    temp = 0
    # 그 학생의 학년에
    for i in range(5):
        temp += total[i][data[student_num][i]-1]

    if max_temp < temp:
        max_temp = temp
        max_student = student_num

print(total)
print(max_student+1)

#
# for class_num in range(5):
#     for i in range(9):


