from utils.readers import read_file_and_split_lines
from typing import *


def do_ranges_overlap_completely(r1: str, r2: str) -> bool:
    range1 = create_range(r1)
    range2 = create_range(r2)
    intersection = set(range2).intersection(range1)
    return len(intersection) == min(len(range2), len(range1))


def do_ranges_overlap(r1: str, r2: str) -> bool:
    range1 = create_range(r1)
    range2 = create_range(r2)
    intersection = set(range2).intersection(range1)
    return len(intersection) > 0


def create_range(raw_range: str) -> Iterable:
    split = raw_range.split('-')
    return range(eval(split[0]), eval(split[1])+1)


def part1(raw: List[List[str]]):
    result = 0
    for line in raw:
        result += 1 if do_ranges_overlap_completely(line[0], line[1]) else 0
    return result


def part2(raw: List[List[str]]):
    result = 0
    for line in raw:
        result += 1 if do_ranges_overlap(line[0], line[1]) else 0
    return result


def main():
    raw = read_file_and_split_lines('input.txt', ',')
    print(f"Part 1: {part1(raw)}")
    print(f"Part 2: {part2(raw)}")


if __name__ == "__main__":
    main()
