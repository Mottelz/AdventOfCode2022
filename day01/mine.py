from typing import List
from utils.readers import read_file_as_strings_without_newline as reader


def convert_list_to_sums(raw: List[str]) -> List[int]:
    out = []
    temp = 0
    for n in raw:
        if n != '':
            temp += eval(n)
        else:
            out.append(temp)
            temp = 0
    return out


def part_one(raw_data: List[str]) -> int:
    return max(convert_list_to_sums(raw_data))


def part_two(raw_data: List[str]) -> int:
    processed = sorted(convert_list_to_sums(raw_data), reverse=True)
    return processed[0] + processed[1] + processed[2]


def main():
    raw_data = reader('input.txt')
    print(f"Part 1: {part_one(raw_data)}")
    print(f"Part 2: {part_two(raw_data)}")


if __name__ == "__main__":
    main()
