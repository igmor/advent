import argparse
import sys
import math
import resource
import copy
import bisect
from collections import defaultdict
from functools import reduce

Beacon = tuple[int, int, int]
Scanner = list[Beacon]

def p20_1(scanners: list[Scanner]) -> int:

    return 0


def parse(lines: list[str]) -> list[Scanner]:
    out = list[Scanner]()
    current_scanner = None
    for l in lines:
        if not l.strip():
            continue
        if not l:
            continue
        if l.startswith('---'):
            if current_scanner:
                out.append(current_scanner)
            current_scanner = Scanner()
            continue
        print(l)
        x, y, z = l.strip().split(',')
        current_scanner.append(Beacon((int(x), int(y), int(z))))
    if current_scanner:
        out.append(current_scanner)

    return out

if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="count the number of increased after decreased depths")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    scanners = parse(lines)
    print(scanners)
    print(p20_1(scanners))

    f.close()

