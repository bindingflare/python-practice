import sys

input = sys.stdin.readline

def solve(T, P, N):
    dp = [0] * (N + 1)

    for i in range(N - 1, -1, -1):
        end = i + T[i]

        if end <= N:
            dp[i] = max(P[i] + dp[end], dp[i + 1])
        else:
            dp[i] = dp[i + 1]

    print(dp[0])

def main():
    N = int(input().strip())
    T = []
    P = []
    
    for i in range(N):
        t, p = map(int, input().split())
        T.append(t)
        P.append(p)
    
    solve(T, P, N)


if __name__ == "__main__":
    main()