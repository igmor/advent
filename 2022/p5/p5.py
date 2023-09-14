from typing import List
import argparse

stacks = [
    ['R', 'W', 'F', 'H', 'T', 'S'], 
    ['W', 'Q', 'D', 'G', 'S'], 
    ['W', 'T', 'B'], 
    ['J', 'Z', 'Q', 'N', 'T', 'W', 'R', 'D'], 
    ['Z', 'T', 'V', 'L', 'G', 'H', 'B', 'F'], 
    ['G', 'S', 'B', 'V', 'C', 'T', 'P', 'L'],
    ['P', 'G', 'W', 'T', 'R', 'B', 'Z'],
    ['R', 'J', 'C', 'T', 'M', 'G', 'N'],
    ['W', 'B', 'G', 'L']
]

def p11(moves: List[List[int]]) -> int:
    for m in moves:
        num, mfrom, mto = m[0], m[1], m[2]
        move = stacks[mfrom-1][:num]
        print(move)
        stacks[mfrom-1] = stacks[mfrom-1][num:]
        stacks[mto-1] =  move[::-1] + stacks[mto-1]

    out = ''
    for s in stacks:
        if s:
            out += s[0]

    return out

def p21(moves: List[List[int]]) -> int:
    for m in moves:
        num, mfrom, mto = m[0], m[1], m[2]
        move = stacks[mfrom-1][:num]
        print(move)
        stacks[mfrom-1] = stacks[mfrom-1][num:]
        stacks[mto-1] =  move + stacks[mto-1]

    out = ''
    for s in stacks:
        if s:
            out += s[0]

    return out

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    moves = []
    for l in lines:
        l = l.replace('\n', '')
        m1, m2, m3, m4, m5, m6 = l.split()
        moves.append([int(m2), int(m4), int(m6)])
    print(len(moves))
    f.close()
    #print(p11(moves))
    print(p21(moves))


