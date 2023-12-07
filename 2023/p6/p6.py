from typing import List, Tuple, Dict
from sortedcontainers import SortedSet
import sys
import bisect
import argparse


def p12(times: List[int], distances: List[int]) -> int:
    total = 1
    for ti, t in enumerate(times):
        nums = 0
        for i in range(1, t):
            v = i
            d = (t - i) * v
            if d > distances[ti]:
                nums += 1

        total *= nums
    return total

def p21(times: int, distance: int) -> int:
    nums = 0
    for i in range(1, times):
        v = i
        d = (times - i) * v
        if d > distance:
            nums += 1

    return nums

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    times = []
    distances = []
    times = lines[0].split(':')[1].strip().split()
    distances = lines[1].split(':')[1].strip().split()
    t1 = ''.join(times)
    d1 = ''.join(distances)
    times = [int(t) for t in times]
    distances = [int(d) for d in distances]
    f.close()
    print(times, distances)
    print(p12(times, distances))
    print(p21(int(t1), int(d1)))
    