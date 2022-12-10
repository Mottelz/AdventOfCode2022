from utils.readers import read_file_and_split_lines
from utils.math import clamp
directions = {'U': [0, 1], 'D': [0, -1], 'L': [-1, 0], 'R': [1, 0]}


def parse_instructions(raw):
    return directions[raw[0]], int(raw[1])


def pos_to_str(pos):
    return f"{str(pos[0])},{str(pos[1])}"


def move_in_direction(position, direction, magnitude):
    position = [position[0] + direction[0] * magnitude, position[1] + direction[1] * magnitude]
    return position


def is_out_of_range(head_pos, tail_pos):
    distance = [abs(head_pos[0] - tail_pos[0]), abs(head_pos[1] - tail_pos[1])]
    if distance[0] > 1 or distance[1] > 1:
        return True
    return False


def get_tail_direction(head_pos, tail_pos):
    rough = [head_pos[0] - tail_pos[0], head_pos[1] - tail_pos[1]]
    return [clamp(rough[0], 1, -1), clamp(rough[1], 1, -1)]


def move_tail(head_pos, tail_pos):
    out = []
    while is_out_of_range(head_pos, tail_pos):
        direction = get_tail_direction(head_pos, tail_pos)
        tail_pos = move_in_direction(tail_pos, direction, 1)
        temp = pos_to_str(tail_pos)
        out.append(temp)
    return out, tail_pos


def part1(instructions):
    head_pos, tail_pos = [0, 0], [0, 0]
    visited = set([pos_to_str(tail_pos)])
    for line in instructions:
        direction, magnitude = parse_instructions(line)
        head_pos = move_in_direction(head_pos, direction, magnitude)
        temp, tail_pos = move_tail(head_pos, tail_pos)
        visited = visited.union(temp)
    return len(visited)


# THIS DOES NOT WORK
# Because the problem was supposed to account for knots that were diagonal last iteration
def part2(instructions):
    ends = [[0, 0] for _ in range(10)]
    visited = set([pos_to_str(ends[-1])])
    for line in instructions:
        direction, magnitude = parse_instructions(line)
        ends[0] = move_in_direction(ends[0], direction, magnitude)
        for i in range(1, len(ends)):
            temp, ends[i] = move_tail(ends[i-1], ends[i])
            if i == len(ends) - 1 and len(temp) > 0:
                visited = visited.union(temp)
    return len(visited)


def main():
    instructions = read_file_and_split_lines('test2.txt', ' ')
    print(f"Part 1: {part1(instructions)}")
    print(f"Part 2: {part2(instructions)}")


if __name__ == "__main__":
    main()
