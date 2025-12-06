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
        if not (l < target < r):
            return
        self.segment_tree[idx] += diff
        if l == r:
            return
        self.update(l, SegmentTree.mid(l,r), idx*2, target, diff)
        self.update(SegmentTree.mid(l,r)+1, r, idx*2+1, target, diff)

    def update_2(self, l, r, idx, target, diff):
        if not (l <= target <= r):
            return
        self.segment_tree[idx] += diff
        if l == r:
            return
        self.update(l, SegmentTree.mid(l,r), idx*2, target, diff)
        self.update(SegmentTree.mid(l,r)+1, r, idx*2+1, target, diff)
            
    def build(self, l: int, r: int, node: T, arr: list[T]) -> None:
        if l == r:
            self.segment_tree[node] = arr[l]
            return

        self.build(l, SegmentTree.mid(l,r), node*2, arr)
        self.build(SegmentTree.mid(l,r)+1, r, node*2+1, arr)
        self.segment_tree[node] = self.segment_tree[node*2] + self.segment_tree[node*2+1]
    
    def print_sum(self, count: int, target: T, l: int, r: int):
        if l == r: # 리프노드 도달
            return l
        
        else:
            if self.segment_tree[target*2] >= count:
                return self.print_sum(count , target*2, l, (l+r)//2)
            else:
                return self.print_sum(count - self.segment_tree[target*2] , target*2 + 1 , (l+r)//2 + 1, r)

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