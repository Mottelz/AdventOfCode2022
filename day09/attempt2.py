from utils.readers import read_file_and_split_lines
from utils.point import Point
directions = {'U': Point(0, 1), 'D': Point(0, -1), 'L': Point(-1, 0), 'R': Point(1, 0)}


def parse_instructions(raw):
    return directions[raw[0]], int(raw[1])


def move_towards(mover, destination):
    visited = []
    distance = destination - mover
    while abs(distance).x > 1 or abs(distance).y > 1:
        mover = mover + distance.direction()
        distance = destination - mover
        visited.append(str(mover))
    return visited, mover


def part2(instructions):
    one = Point(0, 0)
    two = Point(0, 0)
    three = Point(0, 0)
    four = Point(0, 0)
    five = Point(0, 0)
    six = Point(0, 0)
    seven = Point(0, 0)
    eight = Point(0, 0)
    nine = Point(0, 0)
    ten = Point(0, 0)
    visited = set([str(nine)])
    for line in instructions:
        direction, magnitude = parse_instructions(line)
        one = one + direction.increase_by_magnitude(magnitude)
        _, two = move_towards(two, one)
        _, three = move_towards(three, two)
        _, four = move_towards(four, three)
        _, five = move_towards(five, four)
        _, six = move_towards(six, five)
        _, seven = move_towards(seven, six)
        _, eight = move_towards(eight, seven)
        _, nine = move_towards(nine, eight)
        temp_visits, ten = move_towards(ten, nine)
        visited = visited.union(temp_visits)
    return len(visited)


def main():
    instructions = read_file_and_split_lines('input.txt', ' ')
    print(f"Part 2: {part2(instructions)}")


if __name__ == "__main__":
    main()
