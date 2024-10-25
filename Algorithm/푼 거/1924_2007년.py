X, Y = map(int, input().split())
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(X - 1):
    Y += month[i]

days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

print(days[(Y % 7)])
