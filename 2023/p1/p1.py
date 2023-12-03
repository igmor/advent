from typing import List
import argparse

def strdigit_to_number(s: str) -> int:
    if s == "one":
        return 1
    if s == "two":
        return 2
    if s == "three":
        return 3
    if s == "four":
        return 4
    if s == "five":
        return 5
    if s == "six":
        return 6
    if s == "seven":
        return 7
    if s == "eight":
        return 8
    if s == "nine":
        return 9
    return 0

def p1(vals: List[str]) -> int:
    total = 0
    for e in vals:
        d1 = 0
        for i in range(len(e)):
            #print(0, e[i:])
            c = e[i]
            if c.isdigit():
                d1 = int(c)
                break
            if e[i:].startswith("one"):
                d1 = 1
                break
            if e[i:].startswith("two"):
                d1 = 2
                break
            if e[i:].startswith("three"):
                d1 = 3
                break
            if e[i:].startswith("four"):
                d1 = 4
                break
            if e[i:].startswith("five"):
                d1 = 5
                break
            if e[i:].startswith("six"):
                d1 = 6
                break
            if e[i:].startswith("seven"):
                d1 = 7
                break
            if e[i:].startswith("eight"):
                d1 = 8
                break
            if e[i:].startswith("nine"):
                d1 = 9
                break
        d2 = 0
        for i in range(len(e)-1, -1, -1):
            #print(1, e[i:])
            c = e[i]
            if c.isdigit():
                d2 = int(c)
                break
            if e[i:].startswith("one"):
                d2 = 1
                break
            if e[i:].startswith("two"):
                d2 = 2
                break
            if e[i:].startswith("three"):
                d2 = 3
                break
            if e[i:].startswith("four"):
                d2 = 4
                break
            if e[i:].startswith("five"):
                d2 = 5
                break
            if e[i:].startswith("six"):
                d2 = 6
                break
            if e[i:].startswith("seven"):
                d2 = 7
                break
            if e[i:].startswith("eight"):
                d2 = 8
                break
            if e[i:].startswith("nine"):
                d2 = 9
                break
        print(d1, d2)
        total += d1*10 + d2
    return total

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    vals = []
    for l in lines:
        l = l.replace('\n', '')
        vals.append(l)
    print(vals)
    print(p1(vals))
    f.close()

