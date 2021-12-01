def read_data():
    with open('input/day_1.txt') as f:
        data = f.read().splitlines()
    data = list(map(int, data))

    return data


def part_1(data):
    return sum(data[i] > data[i - 1] for i in range(1, len(data)))


def part_2(data):
    return sum(data[i] > data[i - 3] for i in range(3, len(data)))

if __name__ == '__main__':
    data = read_data()
    ans_1 = part_1(data)
    ans_2 = part_2(data)
    print(ans_1)
    print(ans_2)
