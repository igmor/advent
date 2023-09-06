import argparse
import sys
import resource
import copy
import bisect
from collections import defaultdict
from sortedcollections import ItemSortedDict


Board = list[list[int]]

d = defaultdict(int)

def make_board(board: Board, mul: int) -> Board:
    cp = [[0 for y in range(len(board[0]*mul))] for x in range(len(board)*mul)]
    for i in range(len(board)*mul):
        for j in range(len(board[0])*mul):
            new_startx = i
            new_starty = j
            x_mul = 0
            y_mul = 0

            if i >= len(board):
                new_startx = int(i % len(board))
                x_mul = int(i/len(board))
            if j >= len(board[0]):
                new_starty = int(j % len(board[0]))
                y_mul = int(j/len(board[0]))

            new_val = (board[new_startx][new_starty] + x_mul + y_mul)
            if new_val > 9:
                new_val = new_val - 9

            cp[i][j] = new_val
    return cp


def p15_1(board: Board, mem: Board, startx, starty :int) -> int:
    print(startx, starty)
    if startx == len(board) - 1 and starty == len(board[0]) - 1:
        return board[startx][starty]

    if mem[startx][starty] != 0:
        return mem[startx][starty]

    mem[startx][starty] = board[startx][starty] + (
        min(
            p15_1(board, mem, startx, starty+1) if starty + 1 < len(board) else sys.maxsize,
            p15_1(board, mem, startx+1, starty) if startx + 1 < len(board[0]) else sys.maxsize,
            p15_1(board, mem, startx-1, starty) if startx - 1 >= 0 else sys.maxsize,
            p15_1(board, mem, startx, starty-1) if starty - 1 >= 0 else sys.maxsize
        )
    )
    return mem[startx][starty]

def search(board: Board) -> int:
    q_set = set()
    def comp(key, value):
        return value

    dist = ItemSortedDict(comp, [])

    for i in range(len(board)):
        for j in range(len(board[0])):
            q_set.add((i,j))
            dist[(i,j)] = sys.maxsize
    dist[(0,0)] = 0
    d = defaultdict(int)

    while q_set:
        if len(q_set) % 10000 == 0:
            print(len(q_set))
        #print(dist)
        cur = dist.items()[0][0]
        q_set.remove(cur)
        d[cur] = dist[cur]

        neirgbors = [(cur[0]-1, cur[1]), (cur[0]+1, cur[1]), (cur[0], cur[1]-1), (cur[0], cur[1]+1)]
        for n in neirgbors:
            if n in q_set:
                alt = dist[cur] + board[n[0]][n[1]]
                if alt < dist[n]:
                    dist[n] = alt
        if cur in dist:
            del dist[cur]

    return d[(len(board)-1, len(board[0])-1)]

        
def p15_2(board, mem, cp: Board, startx, starty :int, mul: int) -> int:
    if startx == len(board)*mul - 1 and starty == len(board[0])*mul - 1:
        new_startx = int(startx % len(board))
        new_starty = int(starty % len(board[0]))

        val = board[new_startx][new_starty] + 2*(mul-1)
        cp[startx][starty] = val
        if val > 9:
            val -= 9
        print("ret val", board[new_startx][new_starty] + 2*(mul-1), new_startx, new_starty, board[new_startx][new_starty], val)
        return val

    if mem[startx][starty] != 0:
        return mem[startx][starty]

    new_startx = startx
    new_starty = starty
    x_mul = 0
    y_mul = 0

    if startx >= len(board):
        new_startx = int(startx % len(board))
        x_mul = int(startx/len(board))
    if starty >= len(board[0]):
        new_starty = int(starty % len(board[0]))
        y_mul = int(starty/len(board[0]))

    new_val = (board[new_startx][new_starty] + x_mul + y_mul)
    print(startx, starty, new_val)
    d[new_val] += 1
    if new_val > 9:
        new_val = new_val - 9

    if (startx  + 1)% mul == 0 and (starty + 1)% mul == 0:
        print(startx, starty, new_val)
    cp[startx][starty] = new_val

    mem[startx][starty] = new_val + (
        min(
            p15_2(board, mem, cp, startx+1, starty, 5) if startx + 1 < len(board)*mul else sys.maxsize,
            p15_2(board, mem, cp, startx, starty+1, 5) if starty + 1 < len(board[0])*mul else sys.maxsize,
        )
    )
    return mem[startx][starty]

def print_board(lines: list[str], cp: Board, mul:int):
    board, mem1 = parse(lines, 5)

    i = 0
    j = 0
    while i < len(board)*mul and j < len(board[0])*mul:
        #print(i ,j , mem[i][j])
        mem1[i][j] = cp[i][j]
        if i == len(board)*mul-1 and j == len(board[0])*mul - 1:
            break
        up = mem[i][j+1] if j < len(board[0])*mul-1 else sys.maxsize
        left = mem[i+1][j] if i < len(board)*mul-1 else sys.maxsize

        if up < left:
            j += 1
        else:
            i += 1
    for l in mem1:
        print("".join(map(lambda x: str(x), l)))

def parse(lines: list[str], mul: int) -> tuple[Board, Board]:
    board = []
    for l in lines:
        board.append(list(map(lambda x: int(x), list(l.strip()))))

    mem = [[0 for y in range(len(board[0]*mul))] for x in range(len(board)*mul)]
    return board, mem

if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="count the number of increased after decreased depths")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    mul = 5
    board, mem = parse(lines, mul)
    cp = make_board(board, mul)
    for l in cp:
        print("".join(map(lambda x: str(x), l)))

    #print(p15_1(cp, mem, 0, 0) - board[0][0])
    print(search(cp))
    #print_board(lines, cp, 5)

    f.close()

