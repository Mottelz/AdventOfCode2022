# This solution is a revised version of https://www.reddit.com/r/adventofcode/comments/zesk40/comment/izafyu9/
from utils.readers import read_file_as_strings_without_newline
import itertools


def get_sizes(commands):
    stack, sizes = [], []
    for line in commands:
        if line == '$ cd ..':
            size = stack.pop()
            sizes.append(size)
            stack[-1] += size
        elif line.startswith('$ cd '):
            stack.append(0)
        elif line[0].isdigit():
            stack[-1] += int(line.split()[0])
    sizes.extend(itertools.accumulate(stack[::-1]))
    return sizes


def part1(sizes):
    return sum(s for s in sizes if s <= 100_000)


def part2(sizes):
    free_space = 70_000_000 - max(sizes)
    target_size = 30_000_000 - free_space
    return min(s for s in sizes if s >= target_size)


def main():
    commands = read_file_as_strings_without_newline('input.txt')
    sizes = get_sizes(commands)
    print(f"Part 1: {part1(sizes)}")
    print(f"Part 2: {part2(sizes)}")


if __name__ == "__main__":
    main()
