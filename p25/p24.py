import argparse
import sys
import math
import resource
import copy
import random
import bisect
from collections import defaultdict
from functools import reduce

Registers = {
    'a': '0',
    'b': '0',
    'x': '0',
    'y': '0', 
    'w': '0',
    'z': '0'
}

instructions = {
    'inp': (0, None),
    'mul': (1, None, None),
    'add': (2, None, None),
    'mod': (3, None, None),
    'div': (4, None, None),
    'eql': (5, None, None)
}

params = [(1, 10, 2), (1, 14, 13), (1, 14, 13), (26, -13, 9), (1, 10, 15), (26, -13, 3), (26, -7, 6), (1, 11, 5), (1, 10, 16), (1, 13, 1), (26, -4, 6), (26, -9, 3), (26, -13, 7), (26, -9, 9)]

def run(n:int, registers):
    if n % 1000000 == 0:
        print(n)
    s = str(n)
    zs = []
    for i in range(len(s)):
        d = int(s[i])
        run_input(registers, params[i][0], params[i][1], params[i][2], d)
        zs.append((d, registers[5]))
    if registers[5] == 0:
        print(s)
    return zs

def run_input(registers, divz, addx, addy, d):
    registers[4] = d
    registers[2] = (registers[5] % 26) + addx
    registers[5] = int(registers[5]/divz)
    registers[2] = 0 if registers[2] == registers[4] else 1
    registers[5] = registers[5]*(25 * registers[2] + 1) + (registers[4]+addy)*registers[2]

def runrun(n:int, instrs: list[str]):
    s = str(n)
    run_program(instrs, s)

def run_program(instrs: list[str], input:str):
    for i in instrs:
        if not i.strip():
            continue
        instr, *ops = i.strip().split()
        if instr == 'inp':
            print(Registers, input)
            Registers[ops[0]] = input[0]
            input = input[1:]
        if instr == 'add':
            op1, op2 = ops[0], ops[1]
            try:
                op2 = int(op2)
            except ValueError as e:
                op2 = int(Registers[op2])
            Registers[op1] = str(int(Registers[op1]) + int(op2))
        if instr == 'mul':
            op1, op2 = ops[0], ops[1]
            try:
                op2 = int(op2)
            except ValueError as e:
                op2 = int(Registers[op2])
            Registers[op1] = str(int(Registers[op1]) * int(op2))
        if instr == 'div':
            op1, op2 = ops[0], ops[1]
            try:
                op2 = int(op2)
            except ValueError as e:
                op2 = int(Registers[op2])
            Registers[op1] = str(int(int(Registers[op1]) / int(op2)))
        if instr == 'mod':
            op1, op2 = ops[0], ops[1]
            try:
                op2 = int(op2)
            except ValueError as e:
                op2 = int(Registers[op2])
            Registers[op1] = str(int(Registers[op1]) % int(op2))
            #print("mod", Registers[op1])
        if instr == 'eql':
            op1, op2 = ops[0], ops[1]
            try:
                op2 = int(op2)
            except ValueError as e:
                op2 = int(Registers[op2])
            if int(Registers[op1]) == int(op2):
                Registers[op1] = str(1)
            else:
                Registers[op1] = str(0)


def sample(lines:list[str]):
    while True:
        s = ""
        for i in range(14):
            if i == 2:
                s += str(x+1 if x+1 < 9 else 1)
                s += '1'
                continue
            if i == 3:
                s += str(x)
                continue
            if i == 5:
                s += str(2 if (x+2) > 9 else x + 2)
                continue

            x = random.randint(1, 9)
            s += str(x)

def p24_1(lines:list[str]) -> int:
    min_z = 10000000000000000000
    
    for i in range(93997999999999, 93997999111111, -1):
        registers = [0 for i in range(6)]
        zs = run(i, registers)
        if registers[5] == 0 and '0' not in str(i):
            print(i, zs)
            print("registers", registers)
            min_z = registers[5]

    return 0
    
def p24_2(lines:list[str]) -> int:
    for i in range(81111379111111, 81111379999999):
        registers = [0 for i in range(6)]
        zs = run(i, registers)
        if registers[5] == 0:
            print(i, zs)
            print("registers", registers)
            min_z = registers[5]
    return 0

if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="count the number of increased after decreased depths")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    print(p24_1(lines))
    print(p24_2(lines))

    f.close()

