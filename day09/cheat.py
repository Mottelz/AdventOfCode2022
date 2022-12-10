from utils.readers import read_file_as_strings

def move(f):
    x = y = 0 
    for line in f:
        direction, distance = line.split()
        for _ in range(int(distance)):
            x += (direction == 'R') - (direction == 'L')
            y += (direction == 'U') - (direction == 'D')
            yield x, y


def follow(head):
    x = y = 0 
    for hx, hy in head:
        if abs(hx - x) > 1 or abs(hy - y) > 1:
            y += (hy > y) - (hy < y)
            x += (hx > x) - (hx < x)
        yield x, y


tenth = second = list(follow(move(read_file_as_strings('input.txt'))))
for _ in range(8):
    tenth = follow(tenth)
print(len(set(second)))
print(len(set(tenth)))
