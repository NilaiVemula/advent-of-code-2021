def read_data():
    with open('input/day_1.txt') as f:
        data = f.read().splitlines()
    data = list(map(int, data))

    return data


def part_1(data):
    counter = sum([1 if data[i] > data[i - 1]
                   else 0 for i in range(1, len(data))])
    return counter


def part_2(data):
    counter = sum([1 if data[i] > data[i - 3]
                   else 0 for i in range(1, len(data))])
    return counter


if __name__ == '__main__':
    data = read_data()
    ans_1 = part_1(data)
    ans_2 = part_2(data)
    print(ans_1)
    print(ans_2)
