from typing import List
import argparse

def p1(l: List[int]):
    nIncreases = 0
    prev_s = l[0]+l[1]+l[2]
    for i in range(1, len(l)-2):
        next_s = l[i] + l[i+1] + l[i+2]
        if next_s > prev_s:
            nIncreases += 1
        prev_s = next_s
    return nIncreases

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="count the number of increased after decreased depths")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    depths = list[int]()
    for l in lines:
        depths.append(int(l))

    print(p1(depths))
    f.close()

