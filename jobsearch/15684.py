import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
# ladder[row][col] = row번째 가로줄에서 col과 col+1을 연결하는 가로선이 있는지
ladder = [[0] * (N + 1) for _ in range(H + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    ladder[a][b] = 1

def simulate():
    """현재 ladder 상태에서 i번 세로선이 i로 내려오는지 확인"""
    for start in range(1, N + 1):
        k = start
        for r in range(1, H + 1):
            if ladder[r][k]:      # 오른쪽으로 이동
                k += 1
            elif k > 1 and ladder[r][k - 1]:  # 왼쪽으로 이동
                k -= 1
        if k != start:
            return False
    return True

answer = -1
limit = 0  # 현재 시도 중인 '추가 가로선 개수' 상한

def dfs(depth, x, y):
    """
    depth: 지금까지 추가한 가로선 개수
    x, y: 다음으로 탐색을 시작할 (row, col) 위치 (중복 방지용)
    """
    global answer, limit

    # limit개를 다 놓았으면, 이제 상태가 올바른지 한 번만 검사
    if depth == limit:
        if simulate():
            answer = depth
            return True
        return False

    # 가로선 놓기 시도
    for r in range(x, H + 1):
        # 같은 행에서는 y부터, 그다음 행은 1부터
        c_start = y if r == x else 1
        for c in range(c_start, N):  # c와 c+1을 연결하므로 c는 1..N-1
            # 이미 가로선이 있거나 바로 옆에 있으면 놓을 수 없음
            if ladder[r][c]:
                continue
            if ladder[r][c - 1]:
                continue
            if ladder[r][c + 1]:
                continue

            ladder[r][c] = 1
            # 가로선은 서로 인접할 수 없으니, 같은 행에서는 c+2부터 보면 됨
            if dfs(depth + 1, r, c + 2):
                return True
            ladder[r][c] = 0

    return False

if __name__ == "__main__":
    # 추가 가로선 개수를 0, 1, 2, 3 순서로 시도
    if simulate():
        print(0)
    else:
        for k in range(1, 4):
            limit = k
            if dfs(0, 1, 1):
                print(answer)
                break
        else:
            print(-1)
