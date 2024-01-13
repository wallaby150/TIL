def input_data():
    N, T, P = map(int, input().split())
    t_list = []

    for _ in range(T):
        start, end = map(int, input().split())
        start_t = (start // 100, start % 100)
        end_t = (end // 100, end % 100)
        t_list.append((start_t, end_t))

    t_list.sort(key=lambda x: (x[0][0], x[0][1], x[1][0], x[1][1]))
    return N, P, t_list

def solve(N, P, t_list):
    is_seated = [[[False] * 101 for _ in range(60)] for _ in range(24)]

    for time in t_list:
        start_h, start_m = time[0]
        end_h, end_m = time[1]
        seat = find_seat(is_seated, N, start_h, start_m)

        for H in range(start_h, end_h + 1):
            if start_h == end_h:
                for M in range(start_m, end_m):
                    is_seated[H][M][seat] = True
                break

            if H == start_h:
                for M in range(start_m, 60):
                    is_seated[H][M][seat] = True
            elif H == end_h:
                for M in range(end_m):
                    is_seated[H][M][seat] = True
            else:
                for M in range(60):
                    is_seated[H][M][seat] = True

    return check_my_time(is_seated, N, P)

def check_my_time(is_seated, N, P):
    total_min = 0
    for H in range(9, 21):
        for M in range(60):
            if not is_seated[H][M][P]:
                total_min += 1
    return total_min

def find_seat(is_seated, N, h, m):
    max_dist = 0
    pos = -1

    for i in range(1, N + 1):
        if not is_seated[h][m][i]:
            dist = calc_dist(is_seated, h, m, i, N)
            if dist > max_dist:
                max_dist = dist
                pos = i

    return pos

def calc_dist(is_seated, h, m, i, N):
    mid_dist = 101
    for next_seat in range(1, N + 1):
        if next_seat == i:
            continue
        if is_seated[h][m][next_seat]:
            d = abs(i - next_seat)
            if d < mid_dist:
                mid_dist = d

    return mid_dist


def main():
    N, P, t_list = input_data()
    answer = solve(N, P, t_list)
    print(answer)

if __name__ == "__main__":
    main()
