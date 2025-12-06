from dataclasses import dataclass, field
import math
from typing import TypeVar, Generic, Optional, Iterable


"""
TODO:
- Trie.push 구현하기
- (필요할 경우) Trie에 추가 method 구현하기
"""


T = TypeVar("T")


@dataclass
class TrieNode(Generic[T]):
    body: Optional[T] = None
    children: list[int] = field(default_factory=lambda: [])
    is_end: bool = False


class Trie(list[TrieNode[T]]):
    def __init__(self) -> None:
        super().__init__()
        self.append(TrieNode(body=None))

    def push(self, seq: Iterable[T]) -> None:
        """
        seq: T의 열 (list[int]일 수도 있고 str일 수도 있고 등등...)

        action: trie에 seq을 저장하기
        """
        current = self[0]
        
        for i, char in enumerate(seq):
            val = ord(char)

            if char == '\n':
                continue
            hit = None

            for j in current.children:
                if self[j].body == val:
                    hit = j
            
            if hit is None:
                index = len(self)
                self.append(TrieNode(body=val))
                current.children.append(index)
                current = self[-1]
            else:
                current = self[hit]
            
        current.is_end = True

    def root(self) -> TrieNode:
        return self[0]

    def orders(self, root: TrieNode) -> int:
        ways = 1

        if root.is_end:
            if len(root.children) == 0:
                return 1
            
            ways = 2
        elif len(root.children) == 1:
            return self.orders(self[root.children[0]])
            
        for child in root.children:
            ways *= self.orders(self[child])

        return ways * math.factorial(len(root.children))
    