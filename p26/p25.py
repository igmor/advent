import argparse
import sys
import math
import resource
import copy
import bisect
from collections import defaultdict
from functools import reduce

def step_right(c: list[list[int]]) -> int:
    n_moves = 0
    can_move = [[0 for i in range(len(c[0]))] for j in range(len(c))]

    for i in range(len(c)):
        moved = False
        first_move = False
        for j in range(len(c[0])):
            next_j = (j+1) % len(c[0])
            if c[i][j] == '>' and c[i][next_j] == '.':
                can_move[i][j] = 1

        for j in range(len(c[0])):
            next_j = (j+1) % len(c[0])
            #print(c[i][j], c[i][next_j])
            if c[i][j] == '>' and c[i][next_j] == '.' and can_move[i][j]:
                #print("right")
                c[i][next_j] = '>'
                c[i][j] = '.'
                n_moves += 1
                moved = True
            else:
                moved = False
    return n_moves
                    
def step_down(c: list[list[int]]) -> list[list[int]]:
    n_moves = 0
    can_move = [[0 for i in range(len(c[0]))] for j in range(len(c))]

    for i in range(len(c[0])):
        moved = False
        first_move = False
        for j in range(len(c)):
            next_j = (j+1) % len(c)
            if c[j][i] == 'v' and c[next_j][i] == '.':
                can_move[j][i] = 1

        for j in range(len(c)):
            next_j = (j+1) % len(c)
            #print(c[j][i], c[next_j][i])
            if c[j][i] == 'v' and c[next_j][i] == '.' and can_move[j][i]:
                #print("down")
                #print((j, i), (next_j, i))
                c[next_j][i] = 'v'
                c[j][i] = '.'
                n_moves += 1
                moved = True
            else:
                moved = False

    return n_moves

def print_field(Cucumbers: list[list[int]]):
    for i in range(len(Cucumbers)):
        print("".join(Cucumbers[i]))

def p25_1(Cucumbers: list[list[int]]) -> int:
    for i in range(1000):
        n_moves = 0
        #print(i, '----------------------------------')

        n_moves += step_right(Cucumbers)
        n_moves += step_down(Cucumbers)
        #print_field(Cucumbers)

        if n_moves == 0:
            print(i)
            break
    return 0


def parse(lines: list[str]) -> list[list[int]]:
    out = list[list[int]]()
    for l in lines:
        out.append(list(l.strip()))

    return out

if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="count the number of increased after decreased depths")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    cucumbers = parse(lines)
    print_field(cucumbers)
    print(p25_1(cucumbers))

    f.close()

