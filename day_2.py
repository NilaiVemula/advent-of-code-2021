import string
import re
def read_data():
    with open('input/day_2.txt') as f:
        data = f.read().splitlines()
    #data = list(map(int, data))
    return data


def part_1(data):
    x_pos = 0
    y_pos = 0
    regex_string = r"([a-z]*) (\d)"
    for line in data:
        direction = re.match(regex_string, line)[1]
        mag = int(re.match(regex_string, line)[2])
        print(direction, mag)
        if direction == 'down':
            y_pos = y_pos + mag
        if direction == 'up':
            y_pos = y_pos - mag
        if direction == 'forward':
            x_pos = x_pos + mag

    return x_pos * y_pos
    #return sum(data[i] > data[i - 1] for i in range(1, len(data)))


def part_2(data):
    aim = 0
    x_pos = 0
    y_pos = 0
    regex_string = r"([a-z]*) (\d)"
    for line in data:
        direction = re.match(regex_string, line)[1]
        mag = int(re.match(regex_string, line)[2])
        print(direction, mag)
        if direction == 'down':
            aim = aim + mag
        if direction == 'up':
            aim = aim - mag
        if direction == 'forward':
            x_pos = x_pos + mag
            y_pos = y_pos + (aim * mag)

    return x_pos * y_pos
    #return sum(data[i] > data[i - 3] for i in range(3, len(data)))

if __name__ == '__main__':
    data = read_data()
    ans_1 = part_1(data)
    ans_2 = part_2(data)
    print(ans_1)
    print(ans_2)
