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
    


import sys


"""
TODO:
- 일단 Trie부터 구현하기
- count 구현하기
- main 구현하기
"""


def count(trie: Trie, query_seq: str) -> int:
    """
    trie - 이름 그대로 trie
    query_seq - 단어 ("hello", "goodbye", "structures" 등)

    returns: query_seq의 단어를 입력하기 위해 버튼을 눌러야 하는 횟수
    """
    pointer = 0
    cnt = 0

    for element in query_seq:
        if len(trie[pointer].children) > 1 or trie[pointer].is_end:
            cnt += 1

        new_index = None # 구현하세요!

        pointer = new_index

    return cnt + int(len(trie[0].children) == 1)


def main() -> None:
    while True:
        t = Trie()
        words = []
        try: N = int(sys.stdin.readline())
        except: break

        for _ in range(N):
            s = sys.stdin.readline().rstrip()
            t.push(s)
            words.append(s)
        result = 0
        #print(t)
        for word in words:
            result += t.contains(word)

        print("%.2f" % (result/N))


if __name__ == "__main__":
    main()