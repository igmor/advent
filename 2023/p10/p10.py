from typing import List, Tuple, Dict
from sortedcontainers import SortedSet
from collections import defaultdict
from math import gcd
import sys
import bisect
import argparse
import functools



def p12(grid: List[List[str]]) -> int:
    total = 0
    s = [-1, -1]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                s = [i, j]
    paths = [[s]]
    while paths:
        p = paths.pop()
        last = p[-1]
        if last == s:
            print(p)
            continue
        i, j = last[0], last[j]
        if grid[i][j] == ".":
            continue
        if grid[i][j] == "S":
            next = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
            for n in next:
                if n[0] < 0 or n[0] >= len(grid) or n[1] < 0 or n[1] >= len(grid[0]):
                    continue
                if grid[n[0]][n[1]] == ".":
                    continue
                if n in p:
                    continue
                paths.append(p + [n])                
        if grid[i][j] == "L":
            if i + 1 < len(grid) and j + 1 < len(grid[0]):
                paths.append(p + [i+1, j+1])                
            continue
        if grid[i][j] == "J":
            continue
        if grid[i][j] == "7":
            continue
        if grid[i][j] == "F":
            continue
        if grid[i][j] == "|":
            continue
        if grid[i][j] == "-":
            continue

    return total

def p21(history: List[List[str]]) -> int:
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    grid = []
    for line in lines:
        l = line.strip().replace('\n', '')
        l = l.split()
        grid.append(list(l))
    f.close()
    print(grid)
    print(p12(grid))
    print(p21(grid))
    