from typing import List, Tuple
import argparse


def p12(cards: List[Tuple[List[int], List[int]]]) -> int:
    total = 0
    for i, c in enumerate(cards):
        wins = set(c[0])
        m = 0
        for yn in c[1]:
            if yn in wins:
                if m:
                    m *= 2
                else:
                    m = 1
        total += m
        
    return total

def p21(cards: List[Tuple[List[int], List[int]]]) -> int:
    total = 0
    total_cards = [1]*len(cards)
    for i, c in enumerate(cards):
        wins = set(c[0])
        mc = 0
        for yn in c[1]:
            if yn in wins:
                mc += 1
        print(mc, c[1])
        for j in range(i+1, min(i+mc+1, len(cards))):
            total_cards[j] += total_cards[i]
    print(total_cards)
    return sum(total_cards)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    cards = []
    for l in lines:
        l = l.replace('\n','')
        win, you = l.strip().split('|')
        _, num_win = win.strip().split(':')
        w = []
        win_numbers = num_win.strip().split()
        for wn in win_numbers:
            w.append(int(wn))
        y = []
        your_numbers = you.strip().split()
        for yn in your_numbers:
            y.append(int(yn))
        cards.append((w, y))
    print(cards)
    f.close()
    print(p12(cards))
    print(p21(cards))


