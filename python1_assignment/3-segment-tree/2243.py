from lib import SegmentTree
import sys


"""
TODO:
- 일단 SegmentTree부터 구현하기
- main 구현하기
"""


def main() -> None:
    input = lambda: sys.stdin.readline().rstrip()
    
    N = 1_000_000
    nums = [0] * (N + 1)
    size = 2**21

    tree = SegmentTree(size)

    M = int(input())
    for _ in range(M):
        order, *content = map(int,input().split())
        if order > 1:
            tree.update(1, N, 1, content[0], content[1])
            nums[content[0]] += content[1]
            
        else:
            eat = tree.count_sum(content[0], 1, 1, N)
            print(eat)
            tree.update(1, N, 1, eat, -1)
            nums[eat] += -1


if __name__ == "__main__":
    main()