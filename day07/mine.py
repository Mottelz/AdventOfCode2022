from utils.readers import read_file_as_strings
from collections import defaultdict


def parse_command(commands, current_command, current_location, filetree):
    parsed = commands[current_command].split(' ')
    if parsed[1] == 'cd':
        if parsed[2] == '/':
            return filetree, "", current_command+1
        elif parsed[2] != '..':
            return filetree, f"{current_location}/{parsed[2]}", current_command+1
        else:
            current_location = current_location.split('/')
            current_location = current_location[:-1]
            current_location = '/'.join(current_location)
            return filetree, current_location, current_command+1
    if parsed[1] == 'ls':
        return add_to_dir(commands, current_command+1, current_location, filetree)


def add_to_dir(commands, current_command, current_location, filetree):
    while current_command < len(commands) and commands[current_command][0] != '$':
        parsed = commands[current_command].split(' ')
        if parsed[0] != 'dir':
            filetree[f"{current_location}/{parsed[1]}"] = int(parsed[0])
        current_command += 1
    return filetree, current_location, current_command


def create_filesystem(commands):
    filetree = {}
    current_location = ''
    current_command = 0
    while current_command < len(commands):
        filetree, current_location, current_command = \
            parse_command(commands, current_command, current_location, filetree)
    return filetree


def get_folder_values(filesystem):
    out = defaultdict(int)
    for file in filesystem:
        out = add_folder_to_files_value(file, out, filesystem[file])
    return out


def add_folder_to_files_value(file, value_list, size):
    if file.count('/') > 1:
        folder_list = file.split('/')[1:-1]
        for i in range(len(folder_list)):
            folder = '/'.join(folder_list[:i+1])
            value_list[folder] += size
    value_list['/'] += size
    return value_list


def part1(folder_values, size):
    out = 0
    for folder in folder_values:
        out += folder_values[folder] if folder_values[folder] < size else 0
    return out


def part2(folder_values, disk_size, space_required):
    free_space = disk_size - folder_values['/']
    target_size = space_required - free_space
    past = 0
    for folder_size in sorted(folder_values.values(), reverse=True):
        if folder_size < target_size:
            return past
        else:
            past = folder_size


def main():
    raw = read_file_as_strings('input.txt')
    filesystem = create_filesystem(raw)
    folder_values = get_folder_values(filesystem)
    print(f"Part 1: {part1(folder_values, 100_000)}")
    print(f"Part 2: {part2(folder_values, 70000000, 30_000_000)}")


if __name__ == "__main__":
    main()
