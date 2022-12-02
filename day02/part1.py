from utils.readers import read_file_as_strings_without_newline
from typing import List

o_key = {'A': 'r', 'B': 'p', 'C': 's'}
p1_key = {'X': 'r', 'Y': 'p', 'Z': 's'}
v = {'r': 1, 'p': 2, 's': 3}


def score_round(a: str, b: str) -> int:
    if a == b:
        return 3
    if a == 'r':
        return 6 if b == 'p' else 0
    if a == 'p':
        return 6 if b == 's' else 0
    if a == 's':
        return 6 if b == 'r' else 0


def part1(data: List[List[str]]) -> int:
    out = 0
    for line in data:
        out += score_round(o_key[line[0]], p1_key[line[1]]) + v[p1_key[line[1]]]
    return out


def parse_input(raw: List[str]) -> List[List[str]]:
    out = []
    for line in raw:
        out.append(line.split())
    return out


def main():
    raw_data = read_file_as_strings_without_newline('input.txt')
    clean = parse_input(raw_data)
    print(part1(clean))


if __name__ == '__main__':
    main()