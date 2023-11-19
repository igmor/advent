from typing import List
import argparse

def p11(rs: List[List[str]]) -> int:
    score = 0
    for r in rs:
        l = len(r)
        t1 = set(list(r[:l//2]))
        t2 = set(list(r[l//2:]))

        item = t1 & t2
        for i in item:
            if i.isupper():
                s = ord(i) - ord('A') + 27
            else:
                s = ord(i) - ord('a') + 1
            score += s
            print(item, s)
    return score

def p21(rs: List[List[str]]) -> int:
    score = 0
    for rg in rs:
        t1 = set(list(rg[0]))
        t2 = set(list(rg[1]))
        t3 = set(list(rg[2]))

        item = t1 & t2 & t3
        for i in item:
            if i.isupper():
                s = ord(i) - ord('A') + 27
            else:
                s = ord(i) - ord('a') + 1
            score += s
            print(item, s)
    return score

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    rs = []

    rsg = []
    i = 1
    group = []
    for l in lines:
        l = l.replace('\n', '')
        group.append(l)
        rs.append(l)
        if i % 3 == 0:
            rsg.append(group)
            group = []
        i += 1
    if group:
        rsg.append(group)
    f.close()
    print(p11(rs))
    print(p21(rsg))


