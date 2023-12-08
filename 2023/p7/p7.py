from typing import List, Tuple, Dict
from sortedcontainers import SortedSet
from collections import defaultdict
import sys
import bisect
import argparse
import functools

cards = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}

def p12(hands: List[List[str]], bids: List[int]) -> int:
    def rank(hand):
        flash = defaultdict(int)
        for i in range(5):
            flash[cards[hand[i]]] += 1
        if len(flash) == 5:
            return 1
        if len(flash) == 4:
            return 2
        if len(flash) == 3:
            if 2 in flash.values():
                return 3
            if 3 in flash.values():
                return 4
        if len(flash) == 2:
            if 2 in flash.values():
                return 5
            if 4 in flash.values():
                return 6
        if len(flash) == 1:
            return 7
        
        raise Exception("Invalid hand")
            
        
    
    def cmp_hand(a, b):
        if cards[a[0]] > cards[b[0]]:
            return 1
        elif cards[a[0]] < cards[b[0]]:
            return -1
        else:
            return 0

    def cmp_hands(a, b):
        h1 = a[0]
        h2 = b[0]
        if rank(h1) > rank(h2):
            return 1
        elif rank(h1) < rank(h2):
            return -1
        else:
            for i in range(5):
                ret = cmp_hand(h1[i], h2[i])
                if ret != 0:
                    return ret
            return 0

    total = 0
    sh = sorted(zip(hands, bids), key=functools.cmp_to_key(cmp_hands))
    for i in range(len(sh)):
        total += sh[i][1] * (i + 1)
    return total

cards1 = {'A': 13, 'K': 12, 'Q': 11, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1, 'J': 0}

def p21(hands: List[List[str]], bids: List[int]) -> int:
    def modified_flash(flash):
        def cmp_internal(a, b):
            if a[1] > b[1]:
                return 1
            elif a[1] < b[1]:
                return -1
            else:
                if cards1[a[0]] > cards1[b[0]]:
                    return 1
                elif cards1[a[0]] < cards1[b[0]]:
                    return -1
                return 0

        if len(flash) == 1:
            return flash # cant improve five of a kind
        
        modified = flash.copy()

        numJ = 0
        if 'J' in modified:
            print('delete', modified)
            numJ = modified['J']
            del modified['J']

        print(modified.items())
        items = sorted(modified.items(), key=functools.cmp_to_key(cmp_internal), reverse=True)
        modified[items[0][0]] += numJ
        print('new', modified.items())

        return modified


    def rank(hand):
        flash = defaultdict(int)
        for i in range(5):
            flash[hand[i]] += 1
        new_flash = modified_flash(flash)
        if new_flash != flash:
            print(new_flash.keys())
            flash_key = ''.join(new_flash.keys())
            replacement_tbl[flash_key] = flash

        if len(new_flash) == 5:
            return 1
        if len(new_flash) == 4:
            return 2
        if len(new_flash) == 3:
            if 2 in new_flash.values():
                return 3
            if 3 in new_flash.values():
                return 4
        if len(new_flash) == 2:
            if 2 in new_flash.values():
                return 5
            if 4 in new_flash.values():
                return 6
        if len(new_flash) == 1:
            return 7
        
        raise Exception("Invalid hand")
            
    
    def cmp_hand(a, b):
        if cards1[a[0]] > cards1[b[0]]:
            return 1
        elif cards1[a[0]] < cards1[b[0]]:
            return -1
        else:
            return 0

    def cmp_hands(a, b):
        h1 = a[0]
        h2 = b[0]
        if rank(h1) > rank(h2):
            return 1
        elif rank(h1) < rank(h2):
            return -1
        else:
            for i in range(5):
                ret = cmp_hand(h1[i], h2[i])
                if ret != 0:
                    return ret
            return 0

    total = 0
    sh = sorted(zip(hands, bids), key=functools.cmp_to_key(cmp_hands))
    for i in range(len(sh)):
        total += sh[i][1] * (i + 1)
    return total

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    hands = []
    bids = []
    for line in lines:
        l = line.strip().replace('\n', '')
        hand, bid = l.split()
        hands.append(list(hand))
        bids.append(int(bid))
    f.close()
    print(hands, bids)
    print(p12(hands, bids))
    print(p21(hands, bids))
    