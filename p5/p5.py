import argparse
from collections import defaultdict

Board = list[list[int]]
Boards = list[list[list[int]]]

def p5_1(seq: list[int], boards):
    bingo_boards = [[[None for x in range(5)] for y in range(5)] for z in range(len(boards))]
    for n in seq:
        for b1, b2 in zip(bingo_boards, boards):
            place(n, b1, b2)
            if is_filled(b1):
                return score(int(n), b1, b2)

def p5_2(seq: list[int], boards):
    bingo_boards = [[[None for x in range(5)] for y in range(5)] for z in range(len(boards))]
    res_n = 0
    res_b1 = None
    res_b2 = None
    filled = [False] * len(boards)
    for n in seq:
        for i, (b1, b2) in enumerate(zip(bingo_boards, boards)):
            if filled[i]:
                continue
            place(n, b1, b2)

            if is_filled(b1):
                res_n = int(n)
                res_b1 = b1
                res_b2 = b2
                filled[i] = True
    for i in range(len(filled[::-1])):
        if filled[i]:
            return score(res_n, res_b1, res_b2)     

    return score(res_n, res_b1, res_b2  )

def score(n:int, b1: Board, b2: Board) -> int:
    s = 0
    for i in range(len(b1)):
        for j in range(len(b1[0])):
            if not b1[i][j]:
                s += int(b2[i][j])
    return s * n

def place(n: int, b1: Board, b2: Board):
    for i in range(len(b1)):
        for j in range(len(b1[0])):
            if b2[i][j] == n:
                b1[i][j] = n

def is_filled(b: Board) -> bool:
    for i in range(len(b)):
        full = True
        for j in range(len(b[0])):
            if not b[i][j]:
                full = False
        if full:
            return True
    for i in range(len(b)):
        full = True       
        for j in range(len(b[0])):
            if not b[j][i]:
                full = False
        if full:
            return True
    return False

def parse(lines: list[str]):
    out = Boards()

    seq = lines[0].split(',')
    board = []
    for l in lines[2:]:
        if l == "\n":
            out.append(board)
            board = []
            continue
        board.append(list(l.split()))
    out.append(board)
    return seq, out

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="count the number of increased after decreased depths")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    bingo_seq, bingo_boards = parse(lines)
    print(p5_1(bingo_seq, bingo_boards))
    print(p5_2(bingo_seq, bingo_boards))
    f.close()

