import string
from utils.readers import read_file_as_strings_without_newline


def get_value(letter):
    if letter in string.ascii_lowercase:
        return ord(letter) - ord('a') + 1
    else:
        return ord(letter) - ord('A') + 27


def get_priority(line):
    s1 = line[:len(line)//2]
    s2 = line[len(line)//2:]
    out = set(s1).intersection(s2)
    return out.pop()


def part1(data):
    sum_of_fancy = 0
    for line in data:
        letter = get_priority(line)
        sum_of_fancy += get_value(letter)
    return sum_of_fancy


def part2(data):
    sum_of_badges = 0
    for n in range(0, len(data), 3):
        badge = set(data[n]).intersection(data[n+1]).intersection(data[n+2]).pop()
        sum_of_badges += get_value(badge)
    return sum_of_badges


def main():
    data = read_file_as_strings_without_newline('input.txt')
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
