from typing import List, Tuple, Callable
import argparse

class Monkey:
    def __init__(self, init_weights: List[int], op: Callable[[int], int], div_test: int, monkey_test_true: int, monkey_test_false: int):
        self.init_items = init_weights
        self.operation = op
        self.test = div_test
        self.dive_test_true = monkey_test_true
        self.dive_test_false = monkey_test_false
        self.num_inspected = 0

    def __str__(self):
        return f'Monkey: {self.init_items}, {self.operation}, {self.test}, {self.dive_test_true}, {self.dive_test_false}, {self.num_inspected}'

def p11(monkeys: List[Monkey]) -> int:
    for r in range(20):
        for i in range(len(monkeys)):
            m = monkeys[i]
            for item in m.init_items:
                m = monkeys[i]
                m.num_inspected += 1
                new_wl = m.operation(item)
                new_wl //= 3
                if new_wl % m.test == 0:
                    print(f'{i} append to {m.dive_test_true}')
                    monkeys[m.dive_test_true].init_items.append(new_wl)
                else:
                    print(f'{i} append to {m.dive_test_false}')
                    monkeys[m.dive_test_false].init_items.append(new_wl)
            m.init_items = []

def p21(moves: List[List[str]]) -> int:
    for r in range(1000):
        for m in monkeys:
            new_items = [m.operation(item, m.test) for item in m.init_items]
            true_items = [item for item in new_items if item % m.test == 0]
            false_items = [item for item in new_items if item % m.test != 0]
            monkeys[m.dive_test_true].init_items.extend(true_items)
            monkeys[m.dive_test_false].init_items.extend(false_items)
            m.init_items.clear()
    

def parse_fn(expr: str) -> Callable[[int], int]:
    tokens = expr.split(' ')
    if tokens[1] == '*':
        if tokens[2] == 'old':
            return lambda x: (x * x)
        else:
            return lambda x: x * int(tokens[2])
    elif tokens[1] == '+':
        if tokens[2] == 'old':
            return (lambda x: x + x)
        else:
            return (lambda x: x + int(tokens[2]))
    elif tokens[1] == '-':
        if tokens[2] == 'old':
            return (lambda x: x - x)
        else:
            return (lambda x: x - int(tokens[2]))
    elif tokens[1] == '/':
        if tokens[2] == 'old':
            return (lambda x: x // x)
        else:
            return (lambda x: x // int(tokens[2]))
    else:
        raise Exception('unexpected fn {}', expr)

def parse_fn2(expr: str) -> Callable[[int, int], int]:
    tokens = expr.split(' ')
    if tokens[1] == '*':
        if tokens[2] == 'old':
            return (lambda x, div: x*x)
        else:
            return (lambda x, div: x * (int(tokens[2])))
    elif tokens[1] == '+':
        if tokens[2] == 'old':
            return (lambda x, div: x)
        else:
            return (lambda x, div: (x + int(tokens[2])))
    elif tokens[1] == '-':
        if tokens[2] == 'old':
            return (lambda x, div: 0)
        else:
            return (lambda x, div: x - int(tokens[2]))
    elif tokens[1] == '/':
        if tokens[2] == 'old':
            return lambda x, div: 1
        else:
            return lambda x, div: x // int(tokens[2])
    else:
        raise Exception('unexpected fn {}', expr)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    f.close()
    init_items = None
    op = None
    dive_test = None
    monkey_test_true = None
    monkey_test_false = None
    monkey = None
    monkeys = []
    i = 0
    for l in lines:
        l = l.replace('\n', '')
        if not l:
            continue
        print(l)
        if l.startswith('Monkey'):
            print(init_items, op, dive_test, monkey_test_true, monkey_test_false)
            if i == 0:
                i += 1
                continue
            else:
                monkey = Monkey(init_items, op, dive_test, monkey_test_true, monkey_test_false)
                monkeys.append(monkey)
                i += 1
        else:
            if l.startswith("  Starting items:"):
                l = l.replace("  Starting items:", "")
                ws = l.split(", ")
                weights = []
                for w in ws:
                    weights.append(int(w))
                init_items = weights
            elif l.startswith("  Operation: new = "):
                l = l.replace("  Operation: new = ", "")
                op = parse_fn2(l)
            elif l.startswith("  Test: divisible by "):
                l = l.replace("  Test: divisible by ", "")
                dive_test = int(l)
            elif l.startswith("    If true: throw to monkey "):
                l = l.replace("    If true: throw to monkey ", "")
                monkey_test_true = int(l)
            elif l.startswith("    If false: throw to monkey "):
                l = l.replace("    If false: throw to monkey ", "")
                monkey_test_false = int(l)
            else:
                raise Exception("unexpected {}", l)

    monkey = Monkey(init_items, op, dive_test, monkey_test_true, monkey_test_false)
    monkeys.append(monkey)
    #p11(monkeys)
    #monkeys = sorted(monkeys, key=(lambda m: m.num_inspected), reverse=True)
    #for m in monkeys:
    #    print(m)
    #print(monkeys[0].num_inspected*monkeys[1].num_inspected)
#    print(p11(monkeys))

    p21(monkeys)
    monkeys = sorted(monkeys, key=(lambda m: m.num_inspected), reverse=True)
    print(monkeys[0].num_inspected*monkeys[1].num_inspected)
