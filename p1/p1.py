from typing import List
import argparse

def p1(l: List[int]):
    nIncreases = 0
    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            nIncreases += 1
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

