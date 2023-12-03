from typing import List, Tuple
import argparse

def is_possible(game: List[List[int]]) -> bool:
    for r in game:
        if r[0] > 12:
            return False
        if r[1] > 13:
            return False
        if r[2] > 14:
            return False
    return True

def power(game: List[List[int]]) -> bool:
    minr = ming = minb = 0
    for r in game:
        minr = max(minr, r[0])
        ming = max(ming, r[1])
        minb = max(minb, r[2])
    print(minr, ming, minb)
    return minr*ming*minb

def p1(vals: List[List[List[int]]]) -> int:
    total = 0
    total_power = 0
    for i, g in enumerate(games):
        if is_possible(games[i]):
            total += i+1
        total_power += power(games[i])
    return total, total_power

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    games = []
    for l in lines:
        game = []
        l = l.replace('\n','')
        gm, rounds = l.split(":")
        print(rounds)
        rounds = rounds.strip().split(";")
        for round in rounds:
            rgb = round.strip().split(",")
            r = [-1, -1, -1]

            for v in rgb:
                num, color = v.strip().split()
                color = color.strip()
                num = num.strip()
                if color == "red":
                    r[0] = int(num)
                if color == "green":
                    r[1] = int(num)
                if color == "blue":
                    r[2] = int(num)
            game.append(r)
        games.append(game)
    print(games)
    print(p1(games))
    f.close()

