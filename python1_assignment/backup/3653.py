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
        
        size = 2**ceil(log(M+N, 2)+1)
        arr = [0]*m + [1]*n
        pos = [0] + [i+m for i in range(n)] # 1-indexed

        tree = SegmentTree(N + M)
        tree.build(0, m+n-1, 1, arr)
        
        moves = list(map(int, input().split()))
        latest = m-1
        def solve() :
  segtree = SegTree(N, M)
  for idx in map(int, input().split()) :
    segtree.search(idx-1)
    segtree.update(idx-1)
  print()
  
for _ in range(int(input())) :
  solve()


if __name__ == "__main__":
    main()