import argparse
import sys
import math
import resource
import copy
import bisect
from collections import defaultdict
from functools import reduce

Board = list[list[int]]
rooms = [[(3,2), (3,3)], [(5,2), (5,3)], [(7,2), (7,3)], [(9,2), (9,3)]]
forbidden = set([(3,1), (5,1), (7,1), (9,1)]

energy = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

def p23_1(board: Board) -> int:
    
    return 0


def p23_2(board: Board) -> int:
    return 0

def parse(lines: list[str]) -> Board:
    out = []
    n = 0
    for l in lines:
        row = list(l.replace('\n',''))
        if n == 0:
            n = len(row)
        if n > 0 and len(row) < n:
            for i in range(len(row), n):
                row.append(' ')
        for i in range(len(row)):
            if row[i] == ' ':
                row[i] = '#' 
        out.append(row)
    return out

if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="count the number of increased after decreased depths")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    board = parse(lines)
    for i in range(len(board)):
        print(board[i])
    print(p23_1(board))
    print(p23_2(board))

    f.close()

