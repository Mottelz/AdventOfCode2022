from utils.point import Point
from utils.readers import read_file_as_strings
directions = {'U': Point(0, 1), 'D': Point(0, -1), 'L': Point(-1, 0), 'R': Point(1, 0)}


def simulate_rope(instructions, end_count):
    heads = [Point(0, 0)] * end_count
    visited = set()
    for line in instructions:
        d, distance = line.split()
        for _ in range(int(distance)):
            heads[0] = heads[0] + directions[d]
            for i in range(1, len(heads)):
                heads[i] = heads[i].move_towards(heads[i-1])
            visited = visited.union([str(heads[-1])])
    return visited


def main():
    instructions = read_file_as_strings('input.txt')
    print(f"Part 1: {len(simulate_rope(instructions, 2))}")
    print(f"Part 2: {len(simulate_rope(instructions, 10))}")


if __name__ == "__main__":
    main()
