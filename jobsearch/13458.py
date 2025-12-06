import sys

input = sys.stdin.readline

def main():
    N = int(input().strip())
    A = list(map(int, input().split()))
    B, C = map(int, input().split())

    total = 0

    for students in A:
        total += 1
        remain = students - B

        if remain > 0:
            total += (remain + C - 1) // C
        
    print(total)

if __name__ == "__main__":
    main()