import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, depth, total):
    global ans
    if depth == 4:
        ans = max(ans, total)
        return

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, total + board[nx][ny])
            visited [nx][ny] = False

def check_t(x, y):
    global ans
    center = board[x][y]

    # ㅗ
    if x - 1 >= 0 and y - 1 >= 0 and y + 1 < M:
        ans = max(ans, center + board[x-1][y] + board[x][y-1] + board[x][y+1])

    # ㅜ
    if x + 1 < N and y - 1 >= 0 and y + 1 < M:
        ans = max(ans, center + board[x+1][y] + board[x][y-1] + board[x][y+1])
    
    # ㅓ
    if x >= 0 and x + 1 < N and y - 1 >= 0:
        ans = max(ans, center + board[x][y-1] + board[x-1][y] + board[x+1][y])
    
    # ㅏ
    if x >= 0 and x + 1 < N and y + 1 < M:
        ans = max(ans, center + board[x][y+1] + board[x-1][y] + board[x+1][y])

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    visited = [[False] * M for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(M):
            visited[i][j] = True
            dfs(i, j, 1, board[i][j])
            visited[i][j] = False
            check_t(i, j)

    print(ans)