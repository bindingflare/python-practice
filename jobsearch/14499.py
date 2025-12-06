import sys
input = sys.stdin.readline

def roll_east(d):
    t, b, n, s, w, e = d
    return [w, e, n, s, b, t]

def roll_west(d):
    t, b, n, s, w, e = d
    return [e, w, n, s, t, b]

def roll_north(d):
    t, b, n, s, w, e = d
    return [s, n, t, b, w, e]

def roll_south(d):
    t, b, n, s, w, e = d
    return [n, s, b, t, w, e]

def main():
    N, M, x, y, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    commands = list(map(int, input().split()))

    dice = [0, 0, 0, 0, 0, 0]

    dx = [0, 0, 0, -1, 1]
    dy = [0, 1, -1, 0, 0]

    for cmd in commands:
        nx = x + dx[cmd]
        ny = y + dy[cmd]

        if not (0 <= nx < N and 0 <= ny < M):
            continue

        if cmd == 1:
            dice = roll_east(dice)
        elif cmd == 2:
            dice = roll_west(dice)
        elif cmd == 3:
            dice = roll_north(dice)
        elif cmd == 4:
            dice = roll_south(dice)

        x, y = nx, ny

        if board[x][y] == 0:
            board[x][y] = dice[1]
        else:
            dice[1] = board[x][y]
            board[x][y] = 0

        print(dice[0])

if __name__ == "__main__":
    main()