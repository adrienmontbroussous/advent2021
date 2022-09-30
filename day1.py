

def part1(path):
    file = open(path)
    compteur = 0
    depth = 10000000
    for row in file:
        previousDepth = depth
        depth = int(row)
        if depth > previousDepth:
            compteur = compteur+1
    return(compteur)


def part2(path):
    file = open(path)
    rfile = file.readlines()
    compteur = 0
    for i in range(0, len(rfile)-3):
        previousDepth = int(rfile[i])
        newDepth = int(rfile[i+3])
        if newDepth > previousDepth:
            compteur = compteur+1
    return(compteur)


print(part1("01.txt"))
print(part2("01.txt"))
