from typing import Dict, List, Tuple, Callable
import argparse
import sys
import ast
import functools
import copy

def draw_chamber(chamber: List[List[int]], bottom):
    for i in range(bottom-1, len(chamber)):
        for j in range(len(chamber[i])):
            if chamber[i][j] == 0:
                print('.', end='')
            else:
                print('#', end='')
        print('')

def p11(result: List[str]) -> int:
    nrocks = 2022
    chamber = matrix = [ [ 0 for i in range(7) ] for j in range(10000) ]
    bottom = len(chamber) - 1

    n = 0
    nsteps = 0
    while nrocks > 0:
        nrocks -= 1
        figures = []
        if n%5 == 0: # ----
            y = bottom - 4
            figures = [(y, 2), (y, 3), (y, 4), (y, 5)]
        elif n%5 == 1: # +
            y = bottom - 6
            figures = [(y, 3), (y+1, 2), (y+1, 3), (y+1, 4), (y+2, 3)]
        elif n%5 == 2: # L
            y = bottom - 6
            figures = [(y, 4), (y+1, 4), (y+2, 4), (y+2, 3), (y+2, 2)]
        elif n%5 == 3: # |
            y = bottom - 7
            figures = [(y, 2), (y+1, 2), (y+2, 2), (y+3, 2)]
        elif n%5 == 4: # []
            y = bottom - 5
            figures = [(y, 2), (y, 3), (y+1, 2), (y+1, 3)]

        while True:
            win_dir = result[nsteps]

            if win_dir == '<':
                bump = False
                new_figures = copy.deepcopy(figures)
                for i in range(len(figures)):
                    if figures[i][1] - 1 >=0 and chamber[figures[i][0]][figures[i][1]-1] == 0:                
                        new_figures[i] = (figures[i][0], figures[i][1]-1)
                    else:
                        bump = True
                if not bump:
                    figures = new_figures
            elif win_dir == '>':
                bump = False
                new_figures = copy.deepcopy(figures)

                for i in range(len(figures)):
                    if figures[i][1] + 1 <= 6 and chamber[figures[i][0]][figures[i][1]+1] == 0:
                        new_figures[i] = (figures[i][0], figures[i][1]+1)
                    else:
                        bump = True
                if not bump:
                    figures = new_figures

            overlap = False
            for i in range(len(figures)):
                x, y  = (figures[i][0]+1, figures[i][1])
                if x == len(chamber) - 1 or chamber[x][y] == 1:
                    overlap = True
                    break
            
            for i in range(len(figures)):
                if overlap:
                    bottom = min(bottom, figures[i][0])
                    chamber[figures[i][0]][figures[i][1]] = 1
                else:
                    figures[i] = (figures[i][0]+1, figures[i][1])
            nsteps += 1
            nsteps = nsteps % len(result)
            if overlap:
                for i in range(len(figures)):
                    bottom = min(bottom, figures[i][0])
                break
        n += 1
    draw_chamber(chamber, bottom)
    return len(chamber) - bottom - 1

def p12(result: List[str]) -> int:
    # periods starts from 628 rocks at 1752 floor(bottom), period length is 1715 rocks = 2711 floors
    # the rest is just trivial math:
    # (1000000000000-628)//1715 = 583090378 periods,
    # 1000000000000 - (583090378 * 1715 + 628) = 1102 rocks left after last period completes
    # 628 + 1102 = 1730 rocks at 2751 floor
    # 583090378 * 2711 + 2751 = 1580758017509 floor at 1000000000000 rocks
    return 1580758017509

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    result = []
    result = list(lines[0])
    print(result, len(result))

    print(p11(result))
    print(p12(result))
