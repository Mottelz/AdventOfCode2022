from utils.readers import read_blocks
from monkey import Monkey


def build_monkey(raw_input: str):
    parsed = raw_input.split('\n')
    items = []
    test_val = 0
    worry_val = 0
    worry_op = ''
    fail_target = 0
    pass_target = 0
    for line in parsed:
        line = line.strip()
        if 'Starting items: ' in line:
            items = [int(n) for n in line[len('Starting items: '):].split(',')]
        elif 'Operation: ' in line:
            temp = line[len('Operation: new = old '):].split(' ')
            worry_op = temp[0]
            worry_val = temp[1]
        elif 'Test: ' in line:
            test_val = eval(line[len('Test: divisible by '):])
        elif 'If true: throw to monkey ' in line:
            pass_target = eval(line[len('If true: throw to monkey '):])
        elif 'If false: throw to monkey ' in line:
            fail_target = eval(line[len('If false: throw to monkey '):])
    return Monkey(test_val, worry_op, worry_val, fail_target, pass_target, items)


def part1(monkeys, rounds):
    for _ in range(rounds):
        for m in range(len(monkeys)):
            while len(monkeys[m]) > 0:
                item, target = monkeys[m].pass_next_item()
                monkeys[target].catch_item(item)
    temp = sorted(monkeys, reverse=True)
    return temp[0].plays * temp[1].plays


def main():
    raw = read_blocks('input.txt')
    monkeys = []
    for line in raw:
        monkeys.append(build_monkey(line))
    print(f"Part 1: {part1(monkeys, 20)}")


if __name__ == '__main__':
    main()
