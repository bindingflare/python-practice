from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Callable


"""
TODO:
- SegmentTree 구현하기
"""


T = TypeVar("T")
U = TypeVar("U")


class SegmentTree(Generic[T, U]):
    segment_tree: list[T] = []
    
    @staticmethod
    def mid(l, r):
        return (l+r) // 2
    
    def __init__(self, size: int):
        self.segment_tree = [0] * size

    def update(self, l, r, idx, target, diff):
        if r < target or target < l:
            return
        self.segment_tree[idx] += diff
        if l == r:
            return
        self.update(l, SegmentTree.mid(l,r), idx*2, target, diff)
        self.update(SegmentTree.mid(l,r)+1, r, idx*2+1, target, diff)

    def update_2(self, l, r, node, IDX, DIFF):
        if not (l <= IDX <= r):
            return
        self.segment_tree[node] += DIFF
        if l == r:
            return
        self.update_2(l, SegmentTree.mid(l,r), node*2, IDX, DIFF)
        self.update_2(SegmentTree.mid(l,r)+1, r, node*2+1, IDX, DIFF)
            
    def build(self, l: int, r: int, node: T, arr: list[T]) -> None:
        if l == r:
            self.segment_tree[node] = arr[l]
            return

        self.build(l, SegmentTree.mid(l,r), node*2, arr)
        self.build(SegmentTree.mid(l,r)+1, r, node*2+1, arr)
        self.segment_tree[node] = self.segment_tree[node*2] + self.segment_tree[node*2+1]
    
    def count_sum(self, count: int, idx: T, l: int, r: int):
        if l == r:
            return l
        
        else:
            if self.segment_tree[idx*2] >= count:
                return self.count_sum(count , idx*2, l, (l+r)//2)
            else:
                return self.count_sum(count - self.segment_tree[idx*2] , idx*2 + 1 , (l+r)//2 + 1, r)

    def interval_sum(self, l, r, node, LEFT, RIGHT):
        if r < LEFT or RIGHT < l: # outside of range [LEFT, RIGHT]
            return 0
        if LEFT <= l and r <= RIGHT:
            return self.segment_tree[node]
        lsum = self.interval_sum(l, SegmentTree.mid(l,r), node*2, LEFT, RIGHT)
        rsum = self.interval_sum(SegmentTree.mid(l,r)+1, r, node*2+1, LEFT, RIGHT)
        return lsum + rsum
    
    def get_ans(self, x, l, r, s, e):
        if e < l or r < s:
            return [0, 0]
        if l <= s and e <= r:
            return self.segment_tree[x]
        mid = (s + e) // 2
        tmp = self.get_ans(x * 2, l, r, s, mid) + self.get_ans(x * 2 + 1, l, r, mid + 1, e)
        tmp.sort(reverse=True)
        return tmp[:2]


import sys


"""
TODO:
- 일단 SegmentTree부터 구현하기
- main 구현하기
"""


class Pair(tuple[int, int]):
    """
    힌트: 2243, 3653에서 int에 대한 세그먼트 트리를 만들었다면 여기서는 Pair에 대한 세그먼트 트리를 만들 수 있을지도...?
    """
    def __new__(cls, a: int, b: int) -> 'Pair':
        return super().__new__(cls, (a, b))

    @staticmethod
    def default() -> 'Pair':
        """
        기본값
        이게 왜 필요할까...?
        """
        return Pair(0, 0)

    @staticmethod
    def f_conv(w: int) -> 'Pair':
        """
        원본 수열의 값을 대응되는 Pair 값으로 변환하는 연산
        이게 왜 필요할까...?
        """
        return Pair(w, 0)

    @staticmethod
    def f_merge(a: Pair, b: Pair) -> 'Pair':
        """
        두 Pair를 하나의 Pair로 합치는 연산
        이게 왜 필요할까...?
        """
        return Pair(*sorted([*a, *b], reverse=True)[:2])

    def sum(self) -> int:
        return self[0] + self[1]


def main() -> None:
    input = sys.stdin.readline

    size = 404040
    n = int(input())
    a = list(map(int, input().split()))
    
    tree = SegmentTree(1, 1, n, size)
    
    m = int(input())
    for query in range(m):
        q, i, j = map(int, input().split())
        if q == 1:
            tree.update(1, 1, n, i, j)
        else:
            ret = tree.get_ans(1, i, j, 1, n)
            print(ret[0] + ret[1])


if __name__ == "__main__":
    main()