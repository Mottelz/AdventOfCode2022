from utils.readers import read_file_as_strings_without_newline
from typing import List


def part1(data: List[str]) -> int:
    values = {
        'A X': 3 + 1,
        'A Y': 6 + 2,
        'A Z': 0 + 3,
        'B X': 0 + 1,
        'B Y': 3 + 2,
        'B Z': 6 + 3,
        'C X': 6 + 1,
        'C Y': 0 + 2,
        'C Z': 3 + 3
    }
    sol = 0
    for game in data:
        sol += values[game]
    return sol


def part2(data: List[str]) -> int:
    values = {
        'A X': 0 + 3,
        'A Y': 3 + 1,
        'A Z': 6 + 2,
        'B X': 0 + 1,
        'B Y': 3 + 2,
        'B Z': 6 + 3,
        'C X': 0 + 2,
        'C Y': 3 + 3,
        'C Z': 6 + 1
    }
    sol = 0
    for game in data:
        sol += values[game]
    return sol


def main():
    raw_data = read_file_as_strings_without_newline('input.txt')
    print(f"Part 1: {part1(raw_data)}")
    print(f"Part 1: {part2(raw_data)}")


if __name__ == '__main__':
    main()