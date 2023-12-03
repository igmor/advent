from typing import Dict, List, Tuple, Callable
import argparse
import sys
import ast
import functools

mmax = 0

def total_flow_rate(tunnels: Dict[str, Tuple[int, str]], visited: Dict[str, bool], flow: List[Tuple[int, int]]) -> int:
    total_fr = 0

    for fl in flow:
       total_fr += fl[0]*fl[1] if fl[0] > 0 else 0

    return total_fr

def flowrate(tunnels: Dict[str, Tuple[int, List[str]]], visited: Dict[str, bool], opened: Dict[str, bool], valve: str, t: int, current_fr: List[Tuple[int, int]]) -> int:
    global mmax

    if t <= 0:
        #print('current valve: ', valve, t, current_fr)
        ss = total_flow_rate(tunnels, visited, current_fr)

        if ss > mmax:
            mmax = ss
        return ss
        
    if len(opened) == len(tunnels):
        print('current valve: ', valve, t, current_fr)
        ss = total_flow_rate(tunnels, visited, current_fr)

        if ss > mmax:
            mmax = ss
        return ss

    #print('current valve: ', valve, t, current_fr, len(opened), len(tunnels))
    fr, tns = tunnels[valve]
        
    opened_valve = []
    t_delta = 0
    opened_val = {valve: False}
    if valve not in opened:
        opened_val = {valve: True}
        opened_valve = [(t-1, fr)]
        t_delta += 1

    #print(tns)
    tns = sorted(tns, key=lambda x: x in opened, reverse=True)
    for tn in tns:
        flowrate(tunnels, visited | {valve: True}, opened | opened_val, tn, t - 1 - t_delta, current_fr + opened_valve)

    ss = total_flow_rate(tunnels, visited, current_fr)

    if ss > mmax:
        mmax = ss


def p11(result: List[Tuple[str, int, str]]) -> int:
    tunnels = dict()
    for t in result:
        tunnels[t[0]] = (t[1], t[2])

    visited = dict()
    opened = dict()
    print(tunnels)
    flowrate(tunnels, visited, opened, 'AA', 30, [])
    return mmax

def p12(result: List[List[Tuple[int, int]]], minx, maxx, miny, maxy: int) -> int:
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    f.close()
    result = []
    for l in lines:
        l = l.replace('\n', '')
        valve, tunnels = l.split(';')
        valve = valve.replace('Valve ', '')
        valve = valve.replace(' has flow rate', '')
        valve, rate = valve.split('=')
        rate = int(rate)
        tunnels = tunnels.replace(' tunnels lead to valves ', '')
        tunnels = tunnels.replace(' tunnel leads to valves ', '')
        tunnels = tunnels.replace(' tunnel leads to valve ', '')
        tunnels = list(map(lambda x: x.strip(), tunnels.split(',')))

        result.append((valve, rate, tunnels))
    print(result)

    print(p11(result))
    #print(p12(result, minx, maxx, miny, maxy))
