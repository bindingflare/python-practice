import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def spread_virus(lab, viruses, N, M):
    temp = [row[:] for row in lab]
    q = deque(viruses)

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                q.append((nx, ny))

    safe = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                safe += 1
    return safe

def main():
    N, M = map(int, input().split())
    lab = [list(map(int, input().split())) for _ in range(N)]

    empties = []
    viruses = []

    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                empties.append((i, j))
            elif lab[i][j] == 2:
                viruses.append((i, j))

    ans = 0
    L = len(empties)

    # 빈 칸 3개 선택 (조합)
    for a in range(L):
        x1, y1 = empties[a]
        lab[x1][y1] = 1
        for b in range(a + 1, L):
            x2, y2 = empties[b]
            lab[x2][y2] = 1
            for c in range(b + 1, L):
                x3, y3 = empties[c]
                lab[x3][y3] = 1

                safe = spread_virus(lab, viruses, N, M)
                if safe > ans:
                    ans = safe

                lab[x3][y3] = 0
            lab[x2][y2] = 0
        lab[x1][y1] = 0

    print(ans)

if __name__ == "__main__":
    main()
