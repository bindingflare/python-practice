PATH_1 = "./python1_assignment/1-divide-and-conquer-multiplication"
PATH_2 = "./python1_assignment/2-trie"
PATH_3 = "./python1_assignment/3-segment-tree"

ROOT_PATH = {
    "10830": PATH_1,
    "3080": PATH_2,
    "5670": PATH_2,
    "2243": PATH_3,
    "3653": PATH_3,
    "17408": PATH_3
}

PATH_SUB = "./python1_assignment/submission"


def f(n: str) -> None:
    num_code = "".join(filter(lambda x: "from lib import" not in x, open(f"{ROOT_PATH[n]}/{n}.py", 'rt', encoding='UTF8').readlines()))
    lib_code = open(f"{ROOT_PATH[n]}/lib.py", 'rt', encoding='UTF8').read()
    code = lib_code + "\n\n\n" + num_code

    open(f"{PATH_SUB}/{n}.py", 'w', encoding='UTF8').write(code)


if __name__ == "__main__":
    for k in ROOT_PATH:
        f(k)