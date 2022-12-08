from utils.readers import read_grid
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def get_visibility(grid, x, y):
    max_x = len(grid)
    max_y = len(grid[0])

    for x_mod, y_mod in directions:
        next_x, next_y = x + x_mod, y + y_mod
        while 0 <= next_x < max_x and 0 <= next_y < max_y and grid[next_x][next_y] < grid[x][y]:
            next_x += x_mod
            next_y += y_mod
        if not(0 <= next_x < max_x and 0 <= next_y < max_y):
            return True
    return False


def get_score(grid, x, y):
    score = 1
    max_x = len(grid)
    max_y = len(grid[0])

    for x_mod, y_mod in directions:
        current = 0
        next_x, next_y = x + x_mod, y + y_mod
        while 0 <= next_x < max_x and 0 <= next_y < max_y:
            current += 1
            if grid[next_x][next_y] >= grid[x][y]:
                break

            next_x += x_mod
            next_y += y_mod
        score *= current
    return score


def part1(grid):
    out = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if get_visibility(grid, x, y):
                out += 1
    return out


def part2(grid):
    out = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            score = get_score(grid, x, y)
            out = max(out, score)
    return out


def main():
    grid = read_grid('input.txt')
    print(f"Part 1: {part1(grid)}")
    print(f"Part 2: {part2(grid)}")


if __name__ == "__main__":
    main()
