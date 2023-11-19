from typing import List
import argparse

def p11(ranges: List[List[int]]) -> int:
    num = 0
    for r in ranges:
        s1, e1, s2, e2 = r[0], r[1], r[2], r[3]
        if s1 >= s2 and s1 <= e2 and e1 <= e2:
            print(r)
            num += 1
            continue
        if s2 >= s1 and s2 <= e1 and e2 <= e1:
            print(r)
            num += 1
            continue

    return num

def p21(ranges: List[List[int]]) -> int:
    num = 0
    for r in ranges:
        s1, e1, s2, e2 = r[0], r[1], r[2], r[3]
        o = min(e1, e2) - max(s1, s2)
        if o >= 0:
            num += 1
    return num


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    ranges = []
    for l in lines:
        l = l.replace('\n', '')
        er1, er2 = l.split(',')
        s1, e1 = er1.split('-')
        s2, e2 = er2.split('-')
        ranges.append([int(s1), int(e1), int(s2), int(e2)])
    print(len(ranges))
    f.close()
    print(p11(ranges))
    print(p21(ranges))


