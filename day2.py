

def part1(path):
    file = open(path)
    rfile = file.readlines()
    depth = 0
    horizontal = 0
    for i in range(0, len(rfile)):
        row = rfile[i].split(" ")
        action = row[0]
        value = int(row[1])
        if action == 'forward':
            horizontal = horizontal+value
        elif action == 'up':
            depth = depth-value
        elif action == 'down':
            depth = depth+value

    return(depth*horizontal)


def part2(path):
    file = open(path)
    rfile = file.readlines()
    depth = 0
    horizontal = 0
    aim = 0
    for i in range(0, len(rfile)):
        row = rfile[i].split(" ")
        action = row[0]
        value = int(row[1])
        if action == 'forward':
            horizontal = horizontal+value
            depth = depth+aim*value
        elif action == 'up':
            aim = aim-value
        elif action == 'down':
            aim = aim+value

    return(depth*horizontal)


print(part1("02.txt"))

print(part2("02.txt"))
