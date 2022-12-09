from utils.readers import *


def get_tops(state: List[List[str]]) -> str:
    out = ''
    for pile in state:
        out += pile.pop(0)
    return out


def parse_instruction(instruction: str) -> (int, int, int):
    inst = instruction.split(' ')
    return int(inst[1]), int(inst[3]) - 1, int(inst[5]) - 1


def part1(state: List[List[str]], instructions: List[str]) -> str:
    for line in instructions:
        count, start, end = parse_instruction(line)
        for i in range(0, count):
            temp = state[start].pop(0)
            state[end].insert(0, temp)
    return get_tops(state)


def part2(state: List[List[str]], instructions: List[str]) -> str:
    for line in instructions:
        count, start, end = parse_instruction(line)
        to_move = state[start][:count]
        state[start] = state[start][count:]
        state[end] = to_move + state[end]
    return get_tops(state)


def main():
    start_state = read_file_and_split_lines('input-start.txt', ',')
    instruction_set = read_file_as_strings_without_newline('input-instructions.txt')
    print(f"Part 1: {part1(start_state, instruction_set)}")
    start_state = read_file_and_split_lines('input-start.txt', ',')
    print(f"Part 2: {part2(start_state, instruction_set)}")


if __name__ == "__main__":
    main()
