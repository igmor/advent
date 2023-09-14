from typing import List
import argparse

def p11(signal: List[str]) -> int:
    buf = ''
    i = 1
    for c in signal:
        print(buf)
        buf += c
        if len(buf) > 4:
            buf = buf[1:]
        if len(set(list(buf))) == 4:
            return i
        i += 1
    return -1

def p21(signal: List[str]) -> int:
    buf = ''
    i = 1
    for c in signal:
        print(buf)
        buf += c
        if len(buf) > 14:
            buf = buf[1:]
        if len(set(list(buf))) == 14:
            return i
        i += 1
    return -1

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    f.close()
    print(p11(lines[0]))
    print(p21(lines[0]))


