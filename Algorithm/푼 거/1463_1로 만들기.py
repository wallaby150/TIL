x = int(input())
lowest_count = 10000


def solve(num, count):
    global lowest_count
    # 너무 많이 연산했으면 패스
    if count >= lowest_count:
        return

    # num이 1이면 lowest_count 갱신
    if num == 1:
        lowest_count = count
        return

    # 연산 시작
    if not num % 3:
        solve(num/3, count+1)
    if not num % 2:
        solve(num/2, count+1)
    solve(num-1, count+1)


solve(x, 0)
print(lowest_count)
