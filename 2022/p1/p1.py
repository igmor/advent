from typing import List
import argparse

def p1(elfs: List[List[int]]) -> int:
    m = 0
    for e in elfs:
        if sum(e) > m:
            m = sum(e)
    return m

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    e = []
    elfs = []
    for l in lines:
        l = l.replace('\n', '')
        if not l:
            elfs.append(e)
            e = []
            continue
        e.append(int(l))

    print(p1(elfs))
    f.close()

