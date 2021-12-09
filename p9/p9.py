import argparse
from collections import defaultdict

Input = list[str]
Output = list[str]
Entry = tuple[Input, Output]
EntryList = list[Entry]

def p9_1(seq: EntryList):
    n = 0
    for i,o in seq:
        for d in o:
            if len(d) in [2, 3, 4, 7]:
                n += 1
    return n

digits = {
    0: set([0, 1, 2, 4, 5, 6]),
    1: set([2, 5]),
    2: set([0, 2, 3, 4, 6]),
    3: set([0, 2, 3, 5, 6]),
    4: set([1, 2, 3, 5]),
    5: set([0, 1, 3, 5, 6]),
    6: set([0, 1, 3, 4, 5, 6]),
    7: set([0, 2, 5]),
    8: set([0, 1, 2, 3, 4, 5, 6]),
    9: set([0, 1, 2, 3, 5, 6])
}

def filter_1(input: Input, d):
    one = None
    for i in input:
        if len(i) == 2:
            one = i
            break
    if one:
        print("one: " + one)
        input.remove(one)
    return input, one

def filter_7(input: Input, one, d):
    seven = None
    for i in input:
        if len(i) == 3:
            seven = i
            c = set(seven) - set(one)
            d[0] = list(c)[0]
            break
    if seven:
        print("seven: " + seven)
        input.remove(seven)
    return input, seven

def filter_4(input: Input, d):
    four = None
    for i in input:
        if len(i) == 4:
            four = i
            break
    if four:
        print("four: " + four)
        input.remove(four)
    return input, four

def filter_9(input: Input, four, d):
    nine = None
    for i in input:
        if len(i) == 6:
            diff = set(i) - (set(i) & (set(four).union(set(d[0]))))
            if len(diff) == 1:
                nine = i
                d[6] = list(diff)[0]
                break
    if nine:
        print("nine: " + nine)
        input.remove(nine)
    return input, nine

def filter_6(input: Input, nine, d):
    six = None
    for i in input:
        if len(i) == 6:
            diff = set(i) - set(nine)
            if len(diff) == 1:
                six = i
                d[4] = list(diff)[0]
                break
    if six:
        print("six: " + six)
        input.remove(six)
    return input, six

def filter_5(input: Input, four, one, d):
    five = None
    for i in input:
        if len(i) == 5:
            diff = set(i) | (set(four) - set(one))
            if diff == set(i):
                five = i
                break
    if five:
        print("five: " + five)
        input.remove(five)
    return input, five

def filter_3(input: Input, seven, d):
    three = None
    for i in input:
        if len(i) == 5:
            diff = set(i) - (set(i) & (set(seven).union(set(d[6]))))
            print(diff)
            if len(diff) == 1:
                three = i
                d[3] = list(diff)[0]
                break
    if three:
        print("three: " + three)
        input.remove(three)
    return input, three

def filter_2(input: Input, three, one, d):
    two = None
    for i in input:
        if len(i) == 5:
            two = i
            diff = set(i) & set(three)
            diff = set(three) - diff
            if len(diff) == 1:
                d[5] = list(diff)[0]
                diff = set(one) - diff
                if len(diff) == 1:
                    d[2] = list(diff)[0]
            break
    if two:
        print("two: " + two)
        input.remove(two)
    return input, two

def filter_8(input: Input, three, d):
    eight = None
    for i in input:
        if len(i) == 7:
            eight = i
            diff = set(i) & (set(three).union(set(d[4])))
            diff = set(i) - diff
            if len(diff) == 1:
                d[1] = list(diff)[0]
            break
    if eight:
        print("eight: " + eight)
        input.remove(eight)
    return input, eight

def filter_0(input: Input, d):
    zero = None
    for i in input:
        if len(i) == 6:
            zero = i
            break
    if zero:
        print("zero: " + zero)
        input.remove(zero)
    return input, zero

def reverse_index(d): 
    out = {}
    for k, v in d.items():
        out[v] = k
    return out

def get_digit(idx, s):
    ss = set()
    for c in s:
        ss.add(idx[c])
    for d, sss in digits.items():
        if sss == ss:
            return str(d)

    return "-1"
    

def infer(input: Input, output: Output):
    d = defaultdict(set)
    input, one = filter_1(input, d)
    input, seven = filter_7(input, one, d)
    input, four = filter_4(input, d)
    input, nine = filter_9(input, four, d)
    input, six = filter_6(input, nine, d)
    input, five = filter_5(input, four, one, d)
    input, three = filter_3(input, seven, d)
    input, two = filter_2(input, three, one, d)
    input, eight = filter_8(input, three, d)
    input, zero = filter_0(input, d)

    idx = reverse_index(d)
    print(input, idx)

    res = ''
    print(output)
    for o in output:
        digit = get_digit(idx, o)
        res += digit
    print(res)

    return int(res)

def p9_2(seq: EntryList):
    n = 0
    for i,o in seq:
        n += infer(i, o)
    return n

def parse(lines: list[str]) -> EntryList:
    
    input = Input()
    output = Output()

    result = EntryList()
    for l in lines:
        i, o = l.split('|')
        input = list(map(lambda x: x.strip(), i.split()))
        output = list(map(lambda x: x.strip(), o.split()))

        result.append((input, output))
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="count the number of increased after decreased depths")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    res = parse(lines)
    print(p9_1(res))
    seq = parse(lines)
    print(p9_2(res))
    f.close()

