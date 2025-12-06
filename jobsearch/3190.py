import sys
from collections import deque

input = sys.stdin.readline

def main():
    N = int(input().strip())
    K = int(input().strip())

    apples = [[False] * N for _ in range(N)]
    for _ in range(K):
        r, c = map(int, input().split())

        apples[r - 1][c - 1] = True

    L = int(input().strip())
    turns = {}
    for _ in range(L):
        X, C = input().split()
        turns[int(X)] = C
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direction = 0

    snake = deque()
    snake.append((0, 0))
    snake_set = set()
    snake_set.add((0, 0))

    time = 0
    x, y = 0, 0

    while True:
        time += 1
        nx = x + dx[direction]
        ny = y + dy[direction]

        if not (0 <= nx < N and 0 <= ny < N):
            print(time)
            return
        
        if (nx, ny) in snake_set:
            print(time)
            return
        
        snake.appendleft((nx, ny))
        snake_set.add((nx, ny))

        if apples[nx][ny]:
            apples[nx][ny] = False
        else:
            tx, ty = snake.pop()
            snake_set.remove((tx, ty))
        
        x, y = nx, ny
    
        if time in turns:
            if turns[time] == 'L':
                direction = (direction - 1) % 4
            else: # 'D'
                direction = (direction + 1) % 4

if __name__ == "__main__":
    main()