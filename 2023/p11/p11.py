from typing import List, Tuple, Dict
from sortedcontainers import SortedSet
from collections import defaultdict
from math import gcd
import sys
import bisect
import argparse
import functools


def get_galaxies(grid: List[List[str]]) -> List[List[int]]:
    galaxies = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "#":
                galaxies.append([i, j])
    return galaxies

def get_crossing_rows(g1: List[int], g2: List[int], e_rows: List[int]) -> int:
    cr = 0
    for r in e_rows:
        if r > g1[0] and r < g2[0]:
            cr += 1
        elif r < g1[0] and r > g2[0]:
            cr += 1
    return cr

def get_crossing_columns(g1: List[int], g2: List[int], e_columns: List[int]) -> int:
    cc = 0
    for c in e_columns:
        if c > g1[1] and c < g2[1]:
            cc += 1
        elif c < g1[1] and c > g2[1]:
            cc += 1
    return cc

def p12(grid: List[List[str]]) -> int:
    total = 0

    e_rows = []
    e_columns = []
    for i in range(len(grid)):
        empty = True
        for j in range(len(grid[i])):
            if grid[i][j] == "#":
                empty = False
                break
        if empty:
            e_rows.append(i)

    for i in range(len(grid[0])):
        empty = True
        for j in range(len(grid)):
            if grid[j][i] == "#":
                empty = False
                break
        if empty:
            e_columns.append(i)
    
    print(e_rows, e_columns)
    galaxies = get_galaxies(grid)
    for i in range(len(galaxies)):
        for j in range(i, len(galaxies)):
            g1 = galaxies[i]
            g2 = galaxies[j]
            d = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
            cr = get_crossing_rows(g1, g2, e_rows)
            cc = get_crossing_columns(g1, g2, e_columns)
            print(d, cr, cc)
            total += (d + cr + cc)
    return total

def p21(history: List[List[str]]) -> int:
    total = 0

    e_rows = []
    e_columns = []
    for i in range(len(grid)):
        empty = True
        for j in range(len(grid[i])):
            if grid[i][j] == "#":
                empty = False
                break
        if empty:
            e_rows.append(i)

    for i in range(len(grid[0])):
        empty = True
        for j in range(len(grid)):
            if grid[j][i] == "#":
                empty = False
                break
        if empty:
            e_columns.append(i)
    
    print(e_rows, e_columns)
    galaxies = get_galaxies(grid)
    for i in range(len(galaxies)):
        for j in range(i, len(galaxies)):
            g1 = galaxies[i]
            g2 = galaxies[j]
            d = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
            cr = get_crossing_rows(g1, g2, e_rows)
            cc = get_crossing_columns(g1, g2, e_columns)
            total += (d + 999999*cr + 999999*cc)
    return total

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    grid = []
    for line in lines:
        l = line.strip().replace('\n', '')
        grid.append(list(l))
    f.close()
    print(grid)
    print(p12(grid))
    print(p21(grid))
    