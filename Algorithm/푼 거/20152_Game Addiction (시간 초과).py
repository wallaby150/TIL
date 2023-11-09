home, pc = map(int, input().split())

def solve(y, x):
    if y > x:
        return 0

    if y == x == home:
        return 1

    if home < pc:
        if home > y or home > x:
            return 0
        return solve(y-1, x) + solve(y, x-1)
    else:
        if home < y or home < x:
            return 0
        return solve(y+1, x) + solve(y, x+1)


print(solve(pc, pc))