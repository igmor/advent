from typing import List
import argparse

def p21(moves: List[List[str]]) -> int:
    score = 0
    for m in moves:
        if m[1] == "X":
            if m[0] == "A":
                score += 3
            elif m[0] == "B":
                score += 1
            else:
                score += 2
        elif m[1] == "Y":
            if m[0] == "A":
                score += 4
            elif m[0] == "B":
                score += 5
            else:
                score += 6
        else:
            if m[0] == "A":
                score += 8
            elif m[0] == "B":
                score += 9
            else:
                score += 7

    return score

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    moves = []
    for l in lines:
        l = l.replace('\n', '')
        moves.append(l.split())
    print(moves)
    f.close()
    print(p21(moves))

