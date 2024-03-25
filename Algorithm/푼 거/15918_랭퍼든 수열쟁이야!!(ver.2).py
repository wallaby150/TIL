N, X, Y = map(int, input().split())
# 어떤 숫자를 사용했는지 확인할 배열
visited = [0] * (N + 1)
# 숫자들을 저장해둘 배열
arr = [0] * (2 * N)
# 결과값
ans = 0
# X와 Y의 값은 같아야 함으로 그사이 들어있는 숫자가 X와 Y에 들어갈 값
arr[Y-1] = arr[X-1] = Y - X - 1
# 위에서 사용한 숫자는 사용 처리
visited[Y-X-1] = 1

# DFS 시작
def solve(idx):
    global ans

    # 마지막 인덱스까지 채웠으면 ans + 1
    if idx == 2 * N:
        ans += 1
        return

    # 이미 채워진 인덱스면 통과
    if arr[idx] != 0:
        solve(idx + 1)

    else:
        # 들어갈 수 있는 숫자를 탐색
        for i in range(1, N+1):
            # 아직 안 썼고, 그 값이 총 길이를 넘지 않으면
            if visited[i] == 0 and idx + i + 1 < 2 * N:
                # 그 넘어 인덱스가 아직 비었으면
                if arr[idx + i + 1] == 0:
                    # 숫자를 기입하고
                    arr[idx] = i
                    arr[idx + i + 1] = i
                    visited[i] = 1
                    # DFS 진행
                    solve(idx + 1)
                    # 기입한 숫자 초기화
                    arr[idx] = 0
                    arr[idx + i + 1] = 0
                    visited[i] = 0

solve(0)
print(ans)