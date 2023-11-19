from typing import List, Tuple
import argparse

ncycle = 0

def tick() -> bool:
    global ncycle
    ncycle += 1
    if (ncycle-20) % 40 == 0 and ncycle <=220:
        return True
    return False

def tick2() -> bool:
    global ncycle
    ncycle += 1
    if ncycle % 40 == 0 and ncycle <=240:
        return True
    return False

def p11(moves: List[List[str]]) -> int:
    x = 1
    global ncycle
    result = 0

    for m in moves:
        if len(m) == 1:
            if tick():
                result += ncycle * x
        else:
            if tick():
                result += ncycle * x
            if tick():
                result += ncycle * x
            x += int(m[1])

    return result

def draw(x, i: int):
    if i >= x - 1 and i <= x+1:
        print('#\t'.expandtabs(1), end = '')
    else:
        print('.\t'.expandtabs(1), end = '')

def p21(moves: List[List[str]]) -> int:
    x = 1
    global ncycle
    ncycle = 0

    cur_move = None
    cur_tick_in_move = 0

    for j in range(6):
        for i in range(40):
            if not cur_move:
                cur_move = moves[0]
                cur_tick_in_move = 0                
                moves = moves[1:]
            if len(cur_move) == 1:
                draw(x, i)
                cur_move = None
            else:
                if cur_tick_in_move == 0:
                    draw(x, i)
                    cur_tick_in_move += 1
                    continue
                else:
                    draw(x, i)
                    x += int(cur_move[1])
                    cur_move = None
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
        moves.append(list(l.split()))
    print(p11(moves))
    p21(moves)

