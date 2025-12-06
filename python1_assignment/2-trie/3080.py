import math
from lib import Trie
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