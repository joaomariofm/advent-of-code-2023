def find_first_number(line):
    for c in line:
        if c.isdigit():
            return c


def find_last_number(line):
    for c in reversed(line):
        if c.isdigit():
            return c


def trebuchet(line):
    if line == '\n':
        return 0

    first_number = find_first_number(line)
    last_number = find_last_number(line)

    return int(first_number + last_number)


with open('./input.txt') as f:
    lines = f.readlines()

    totalSum = 0

    for line in lines:
        sum = trebuchet(line)
        totalSum += sum

    print(totalSum)
