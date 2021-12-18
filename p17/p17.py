import argparse
import sys
import resource
import copy
import bisect
from collections import defaultdict
from functools import reduce

hex_to_binary = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'    
}

d = defaultdict(int)

def parse_litaral(bin:str) -> tuple[int, int, str]:
    out = ''
    end = bin
    i = 0
    while len(end) > 0 and end[0] == '1':
        out += end[1:5]
        i += 5
        end = end[5:]
    if len(end) > 0:
        out += end[1:5]
        i += 5
        end = end[5:]
    return i, int(out,2), end

def parse_operator(bin:str) -> tuple[int, int, list[str], str]:
    total = 0
    out = []

    version = 0
    if bin[0] == '0':
        total_length = int(bin[1:16], 2)
        bin = bin[16:]
        i = 0
        total += 16
        while i < total_length:
            tp, v, length, ops, bin = parse_packet(bin)
            total += length
            i += length
            version += v
            out.append((tp, ops))
    else:
        total_packets = int(bin[1:12], 2)
        bin = bin[12:]
        total += 12
        for i in range(total_packets):
            tp, v, length, ops, bin = parse_packet(bin)
            total += length
            version += v
            out.append((tp, ops))
    return version, total, out, bin
    
def parse_packet(bin:str) -> tuple[int, int, int, list[str], str]:
    packet_version = bin[:3]
    packet_type = int(bin[3:6], 2)

    bin = bin[6:]
    out = []
    total = 6

    version = 0
    if packet_type == 4:
        length, literal_val, bin = parse_litaral(bin)
        out.append(literal_val)
        total += length
    else:
        version, length, ops, bin = parse_operator(bin)
        out.append(ops)
        total += length

    return packet_type, int(packet_version,2) + version, total, out, bin

def p16_1(bin:str) -> list[str]:
    tp, version, length, ops, bin = parse_packet(bin)
    return tp, ops, version

def compute(packet) -> int:
    print("packet:", packet)
    if type(packet) == int:
        return packet
    if type(packet) == list and len(packet) == 1:
        return compute(packet[0])

    op, ops = packet
    print("packet:", op, ops)

    if op == 4:
        return ops[0]

    if type(ops) == list and len(ops) == 1:
        return compute((op, ops[0]))
    if type(ops) == tuple:
        return compute((op, [compute(ops)]))

    if type(ops) == int:
        ops = [ops]
        
    if op == 0:
        args = []
        for o in ops:
            args.append(compute(o))
        return sum(args)
    if op == 1:
        args = []
        for o in ops:
            args.append(compute(o))
        return reduce(lambda x, y: x * y, args)
    if op == 2:
        args = []
        for o in ops:
            args.append(compute(o))
        return min(args)
    if op == 3:
        args = []
        for o in ops:
            args.append(compute(o))
        return max(args)
    if op == 5:
        return 1 if compute(ops[0]) > compute(ops[1]) else 0
    if op == 6:
        return 1 if compute(ops[0]) < compute(ops[1]) else 0
    if op == 7:
        return 1 if compute(ops[0]) == compute(ops[1]) else 0
    

def p16_2(bin:str) -> list[str]:
    tp, version, length, ops, bin = parse_packet(bin)
    return compute((tp, ops))

def parse(lines: list[str]) -> str:
    out = ''
    for c in lines[0].strip():
        out += hex_to_binary[c] 
    print(out)
    return out

if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="count the number of increased after decreased depths")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    bin = parse(lines)
    print(p16_1(bin))
    print(p16_2(bin))

    f.close()

