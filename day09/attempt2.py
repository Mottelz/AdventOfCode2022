from utils.readers import read_file_and_split_lines
from utils.point import Point
directions = {'U': Point(0, 1), 'D': Point(0, -1), 'L': Point(-1, 0), 'R': Point(1, 0)}


def parse_instructions(raw):
    return directions[raw[0]], int(raw[1])


def move_towards(mover, destination, old_dest):
    visited = []
    distance = destination - mover
    while abs(distance).x > 1 or abs(distance).y > 1:
        # old_distance = old_dest - mover
        # if abs(old_distance).x == 1 and abs(old_distance).y == 1:
        #     mover = mover + old_distance.direction()
        #     distance = old_dest - mover
        # else:
        mover = mover + distance.direction()
        distance = destination - mover
        visited.append(str(mover))
    return visited, mover


def part2(instructions, number_of_knots):
    knots = [Point(0, 0)] * number_of_knots
    visited = set([str(knots[-1])])
    for line in instructions:
        direction, magnitude = parse_instructions(line)
        knots[0] = direction.increase_by_magnitude(magnitude)
        old_knots = knots.copy()
        for k in range(1, len(knots)):
            v, knots[k] = move_towards(knots[k], knots[k-1], old_knots[k-1])
            if k == len(knots) - 1 and len(v) > 0:
                visited = visited.union(v)
    return len(visited)


def main():
    instructions = read_file_and_split_lines('test2.txt', ' ')
    print(f"Part 2: {part2(instructions, 10)}")


if __name__ == "__main__":
    main()
