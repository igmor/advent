import argparse
import sys
from collections import defaultdict

def p8_1(seq: list[int]):
    m = sys.maxsize
    pos = -1
    mmax = max(seq)
    mmin = min(seq)
    for j in range(mmin, mmax+1):
        tot_fuel = 0
        for i in range(len(seq)):
            tot_fuel += abs(seq[i] - j)

        if tot_fuel < m:
            m = tot_fuel
            pos = seq[i]
    return m, pos

def p8_2(seq: list[int]):
    m = sys.maxsize
    pos = -1
    mmax = max(seq)
    mmin = min(seq)

    for j in range(mmin, mmax+1):
        tot_fuel = 0
        for i in range(len(seq)):
            n = max(seq[i], j) - min(seq[i], j)
            fuel = ((1 + n) * n) / 2
            tot_fuel += int(fuel)

        if tot_fuel < m:
            m = tot_fuel
            pos = seq[i]
    return m, pos

def parse(lines: list[str]):
    return list(map(lambda x: int(x), lines[0].strip().split(',')))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="count the number of increased after decreased depths")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    seq = parse(lines)
    print(p8_1(seq))
    seq = parse(lines)
    print(p8_2(seq))
    f.close()

