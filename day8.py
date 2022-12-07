

def part1(path):
    file = open(path)
    data = file.read().splitlines()
    data[0]
    lengthAccepted = [2, 3, 4, 7]
    count = 0
    for row in data:
        inputData, ouputData = row.split("|")
        outputSegments = ouputData.split(" ")
        for segment in outputSegments:
            if len(segment) in lengthAccepted:
                print(segment)
                count = count+1
    return(count)


print(part1("day8.txt"))

# 543


def part1(path):
    file = open(path)
    data = file.read().splitlines()
    data[0]
    lengthAccepted = [2, 3, 4, 7]
    count = 0
    for row in data:
        inputData, ouputData = row.split("|")
        outputSegments = ouputData.split(" ")
        for segment in outputSegments:
            if len(segment) in lengthAccepted:
                print(segment)
                count = count+1

    return(count)


print(part2("day8.txt"))
