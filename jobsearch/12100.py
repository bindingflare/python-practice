import sys
input = sys.stdin.readline

def compress_line(line, n):
    tmp = [x for x in line if x != 0]
    res = []
    skip = False

    for i in range(len(tmp)):
        if skip:
            skip = False
            continue

        if i + 1 < len(tmp) and tmp[i] == tmp[i + 1]:
            res.append(tmp[i] * 2)
            skip = True

        else:
            res.append(tmp[i])
    
    while len(res) < n:
        res.append(0)
    return res

def move_left(board, n):
    new_board = []
    for r in range(n):
        new_board.append(compress_line(board[r], n))
    return new_board

def move_right(board, n):
    new_board = []
    for r in range(n):
        reversed_row = board[r][::-1]
        compressed = compress_line(reversed_row, n)
        new_board.append(compressed[::1])
    return new_board

def move_up(board, n):
    new_board = [[0] * n for _ in range(n)]
    for c in range(n):
        col = [board[r][c] for r in range(n)]
        compressed = compress_line(col, n)
        for r in range(n):
            new_board[r][c] = compressed[r]
    return new_board

def move_down(board, n):
    new_board = [[0] * n for _ in range(n)]
    for c in range(n):
        col = [board[r][c] for r in range(n)][::-1]
        compressed = compress_line(col, n)
        compressed = compressed[::-1]
        for r in range(n):
            new_board[r][c] = compressed[r]
    return new_board

def get_max_tile(board, n):
    return max(max(row) for row in board)

def dfs(board, depth, n):
    if depth == 5:
        return get_max_tile(board, n)

    ans = 0

    boards = [
        move_up(board, n),
        move_down(board, n),
        move_left(board, n),
        move_right(board, n)
    ]

    for nb in boards:
        ans = max(ans, dfs(nb, depth + 1, n))
    return ans

def main():
    n = int(input().strip())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    result = dfs(board, 0, n)
    print(result)

if __name__ == "__main__":
    main()
