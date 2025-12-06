import sys
from collections import deque

input = sys.stdin.readline

def move(x, y, dx, dy, board):
    count = 0
    while True:
        nx = x + dx
        ny = y + dy
        
        if board[nx][ny] == "#":
            break
           
        x, y = nx, ny
        count += 1
        
        if board[nx][ny] == "O":
            return x, y, count, True
        
    return x, y, count, False

def bfs(board, rx, ry, bx, by, n, m):
    visited = set()
    visited.add((rx, ry, bx, by))
    
    q = deque()
    q.append((rx, ry, bx, by, 0))
    
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while q:
        rx, ry, bx, by, depth = q.popleft()
        
        if depth >= 10:
            continue
           
        for dx, dy in dirs:
            nrx, nry, rcount, red_hole = move(rx, ry, dx, dy, board)
            nbx, nby, bcount, blue_hole = move(bx, by, dx, dy, board)
        
            if blue_hole:
                continue
            if red_hole and not blue_hole:
                return depth + 1
            
            if nrx == nbx and nry == nby:
                if rcount > bcount:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy
            state = (nrx, nry, nbx, nby)
            if state not in visited:
                visited.add(state)
                q.append((nrx, nry, nbx, nby, depth + 1))
    return -1

def main():
    n, m = map(int, input().split())
    board = []
    rx = ry = bx = by = -1
    
    for i in range(n):
        row = list(input().rstrip())
        for j, ch in enumerate(row):
            if ch == "R":
                rx, ry = i, j
                row[j] = "."
            elif ch == "B":
                bx, by = i, j
                row[j] = "."
        board.append(row)
        
    result = bfs(board, rx, ry, bx, by, n, m)
    print(result)
 
if __name__ == "__main__":
    main()