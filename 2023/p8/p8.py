from typing import List, Tuple, Dict
from sortedcontainers import SortedSet
from collections import defaultdict
from math import gcd
import sys
import bisect
import argparse
import functools


def p12(instructions: List[str], nodes: Dict[str, Tuple[str, str]]) -> int:
    total = 0
    start = 'AAA'
    end = 'ZZZ'

    i = 0
    while start != end:
        move = instructions[i % len(instructions)]
        total += 1
        if move == 'L':
            start = nodes[start][0]
        else:
            start = nodes[start][1]
        i += 1
    return total

def p21(instructions: List[str], nodes: Dict[str, Tuple[str, str]]) -> int:
    total = 0
    starts = [a for a in nodes.keys() if a[-1] == 'A']
    print(len(instructions))

    totals = []
    for j in range(len(starts)):
        total = 0
        i = 0
        s = starts[j]
        while s[2] != 'Z':
            move = instructions[i % len(instructions)]
            total += 1
            if move == 'L':
                s = nodes[s][0]
            else:
                s = nodes[s][1]
            i += 1
        totals.append(total)
    lcm = 1
    for i in totals:
        lcm = lcm*i//gcd(lcm, i)        
    return lcm

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    nodes = {}
    instructions = list(lines[0].strip().replace('\n', ''))
    for line in lines[2:]:
        l = line.strip().replace('\n', '')
        node, lrnodes = l.strip().split('=')
        lrnodes = lrnodes.strip()[1:len(lrnodes)-2]
        l, r = lrnodes.split(',')
        print(l, r)
        nodes[node.strip()] = (l.strip(), r.strip())
    f.close()
    print(instructions, nodes)
    print(p12(instructions, nodes))
    print(p21(instructions, nodes))
    