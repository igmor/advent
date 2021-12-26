import argparse
import sys
import math
import resource
import copy
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

def run_program(instrs: list[str], input:str):
    for i in instrs:
        #print(i, Registers)
        instr, *ops = i.strip().split()
        if instr == 'inp':
            Registers[ops[0]] = input[0]
            input = input[1:]
        if instr == 'add':
            op1, op2 = ops[0], ops[1]
            try:
                op2 = int(op2)
            except ValueError as e:
                op2 = int(Registers[op2])
            #print(i, ops, op1, op2, Registers[op1])
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


def p24_1(lines:list[str]) -> int:
    for i in range(11111111111111, 99999999999999, 26):
        for k,v in Registers.items():
            Registers[k] = 0
        run_program(lines, str(i))
        if i % 10000 == 0:
            print(i)
        if Registers['z'] == '0':
            print(i)
            break
    return 0
    
def p24_2(lines:list[str]) -> int:
    return 0

if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="count the number of increased after decreased depths")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    print(p24_1(lines))
    #print(p24_2(img, algo))

    f.close()

