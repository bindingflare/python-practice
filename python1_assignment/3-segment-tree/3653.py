from lib import SegmentTree
import sys
from math import ceil, log


"""
TODO:
- 일단 SegmentTree부터 구현하기
- main 구현하기
"""


def main() -> None:
    
    input = lambda: sys.stdin.readline().rstrip()

    def mid(l, r):
        return (l+r) // 2

    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())

        size = M+N
        
        tree_size = 2**ceil(log(size, 2)+1)
        arr = [0]*M + [1]*N
        pos = [0] + [i+M for i in range(N)] # 1-indexed

        tree: SegmentTree[int, int] = SegmentTree(tree_size)
        tree.build(0, size-1, 1, arr)
        
        moves = list(map(int, input().split()))
        latest = M-1
        for i in moves:
            tree.update_2(0, size-1, 1, pos[i], -1)
            print(tree.interval_sum(0, size-1, 1, 0, pos[i]-1), end=' ')
            pos[i] = latest
            latest -= 1
            tree.update(0, size-1, 1, pos[i], +1)
        print()


if __name__ == "__main__":
    main()