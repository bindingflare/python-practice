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
        node = self.root()
        for w in seq:
            if w not in [x.body for x in node.children]:
                new = TrieNode(w)
                node.children.append(new)
                node = new
            else:
                node = node.children[[x.body for x in node.children].index(w)]
        node.is_end = True


    def root(self) -> TrieNode:
        return self[0]

    def orders(self, node: TrieNode) -> int:
        ways = 1

        if node.is_end:
            if len(node.children) == 0:
                return 1
            
            ways = 2

        while len(node.children) == 1:
            node = node.children[0]
            
        for child in node.children:
            if not child.is_end:
                ways *= self.orders(child)

        return ways * math.factorial(len(node.children)) % 1_000_000_007
    
    def contains(self, word):
        cnt = 0
        cur = self.root()
        for w in word:
            cur = cur.children[[x.body for x in cur.children].index(w)]

            if len(cur.children) > 1 or cur.is_end:
                cnt+=1
        return cnt
    


import math
import sys
sys.setrecursionlimit(1000000)


"""
TODO:
- 일단 Trie부터 구현하기
- main 구현하기

힌트: 한 글자짜리 자료에도 그냥 str을 쓰기에는 메모리가 아깝다...
""" 

def main() -> None:
    count = int(sys.stdin.readline())

    names = list(sys.stdin.readlines())

    t = Trie()

    names.sort()
    pre = 0
    post = 0

    for i in range(count):
        if i == count - 1:
            #print(names[i][:pre + 1])
            t.push(names[i][:pre + 1])
        else:
            for j in range(len(names[i])):
                if names[i][j] != names[i+1][j]:
                    post = j
                    break

                post = j

            #print(names[i][:max(pre, post)+1])
            t.push(names[i][:max(pre, post)+1])
            pre = post
    
    #print(t.root())
    print(t.orders(t.root()))


if __name__ == "__main__":
    main()