from utils.readers import read_one_line


def contains_repeats(window: str) -> bool:
    for c in window:
        if window.count(c) > 1:
            return True
    return False


def find_start_packet(datastream: str, window_size: int) -> int:
    for i in range(window_size, len(datastream)):
        window = datastream[i-window_size:i]
        if not contains_repeats(window):
            return i


def main():
    datastream = read_one_line('input.txt')
    print(f"Part 1: {find_start_packet(datastream, 4)}")
    print(f"Part 2: {find_start_packet(datastream, 14)}")


if __name__ == "__main__":
    main()
