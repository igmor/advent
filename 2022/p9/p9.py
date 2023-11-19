from typing import List, Tuple
import argparse

rope1 = [[500, 500], [500, 500]]
rope2 = [[500, 500], [500, 500], [500, 500], [500, 500], [500, 500], [500, 500], [500, 500], [500, 500], [500, 500], [500, 500]]

def make_head(m: Tuple[str, str], rope: List[List[int]]):
    start_hx = rope[0][0]
    start_hy = rope[0][1]
    if m[0] == 'U':
        start_hy += int(m[1])
    elif m[0] == 'D':
        start_hy -=int(m[1])
    elif m[0] == 'L':
        start_hx -= int(m[1])
    elif m[0] == 'R':
        start_hx += int(m[1])
    else:
        raise Exception('unexpected move')
    rope[0][0] = start_hx
    rope[0][1] = start_hy

    
def move_tail(grid: List[List[int]], rope: List[List[int]], knot: int):
    start_hx = rope[knot-1][0]
    start_hy = rope[knot-1][1]
    start_tx = rope[knot][0]
    start_ty = rope[knot][1]

    if start_hx == start_tx:
        if abs(start_hy - start_ty) == 2:
            d = (start_hy - start_ty) // 2
            start_ty += d
    elif start_hy == start_ty:
        if abs(start_hx - start_tx) == 2:
            d = (start_hx - start_tx) // 2
            start_tx += d
    else:
        if abs(start_hy - start_ty) == 2 and abs(start_hx - start_tx) == 2:
            d1 = (start_hy - start_ty) // 2
            d2 = (start_hx - start_tx) // 2
            start_ty += d1
            start_tx += d2 
        if abs(start_hy - start_ty) == 2:
            d = (start_hy - start_ty) // 2
            start_ty += d 
            start_tx = start_hx
        elif abs(start_hx - start_tx) == 2:
            d = (start_hx - start_tx) // 2
            start_tx += d
            start_ty = start_hy
        #else:
        #    raise Exception(f'wrong condition {start_hx}, {start_hy}, {start_tx}, {start_ty}')
    if knot == 9: #tail
        grid[start_tx][start_ty] = 1
    rope[knot][0] = start_tx
    rope[knot][1] = start_ty

def num_pos(grid: List[List[int]]) -> int:
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            total += grid[i][j]
    return total

def p11(grid: List[List[int]], moves: List[Tuple[str, int]]) -> int:
    for m in moves:
        for i in range(int(m[1])):
            print(f'move to {rope1}')

            make_head((m[0], 1), rope1)
            move_tail(grid, rope1, 1)
    return num_pos(grid)

def p21(grid: List[List[int]], moves: List[Tuple[str, int]]) -> int:
    for m in moves:
        print(f'move {m} for rope {rope2}')
        for i in range(int(m[1])):
            make_head((m[0], 1), rope2)
            for i in range(1, len(rope2)):
                move_tail(grid, rope2, i)
    return num_pos(grid)

def print_pr(something: List[List[int]]):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                print('.', end="")
            else:
                print('#', end="")
        print('\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    f.close()
    moves = []
    for l in lines:
        l = l.replace('\n', '')
        moves.append(l.split())
    grid = [[0 for x in range(1000)] for y in range(1000)]
    print(p11(grid, moves))
    grid = [[0 for x in range(1000)] for y in range(1000)]

    print(p21(grid, moves))


