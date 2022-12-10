from utils.readers import read_file_as_strings


def sum_update(clock, first, increment, reg):
    temp = clock - first
    if clock == first or (temp % increment == 0 and temp > 0):
        return reg * clock
    return 0


def draw_pixel(clock, cursor):
    curr = clock % 40
    if curr == 0 and clock > 0:
        print('')
    if curr in [cursor-1, cursor, cursor+1]:
        print('#', end='')
    else:
        print('.', end='')


def part1(instructions, first, increment):
    reg = 1
    clock = 0
    sum = 0
    for line in instructions:
        if line == 'noop':
            clock += 1
            sum += sum_update(clock, first, increment, reg)
        else:
            clock += 1
            sum += sum_update(clock, first, increment, reg)
            clock += 1
            sum += sum_update(clock, first, increment, reg)
            reg += int(line.split(' ')[1])
    return sum


def part2(instructions):
    clock = 0
    cursor = 1
    for line in instructions:
        draw_pixel(clock, cursor)
        clock += 1
        if line != 'noop':
            draw_pixel(clock, cursor)
            clock += 1
            cursor += int(line.split(' ')[1])


def main():
    instructions = read_file_as_strings('input.txt')
    print(f"Part 1: {part1(instructions, 20, 40)}")
    print("=========Part 2==========")
    part2(instructions)


if __name__ == "__main__":
    main()
