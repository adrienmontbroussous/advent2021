

def part1(path):
    file = open(path)
    data = file.read().splitlines()
    textInput = data[0]
    rules = {}
    nbIteration = 10
    for i in range(2, len(data)):
        parents, enfant = data[i].split(' -> ')
        rules[parents] = enfant
    for k in range(nbIteration):
        textMaj = ""
        for i in range(len(textInput)-1):
            if textInput[i:i+2] in rules.keys():
                if i == 0:
                    textMaj = textInput[i] + \
                        rules[textInput[i:i+2]]+textInput[i+1]
                else:
                    textMaj = textMaj + \
                        rules[textInput[i:i+2]]+textInput[i+1]
            else:
                if i == 0:
                    textMaj = textInput[i]+textInput[i+1]
                else:
                    textMaj = textMaj+textInput[i+1]
        textInput = textMaj
    freq = {}
    for c in set(textMaj):
        freq[c] = textMaj.count(c)
    return(max(freq.values())-min(freq.values()))


print(part1("day14.txt"))

# 2899

# part 2 is the same with 40 iteration, we have to make a code with better performances.
# instead of stockings string we wille store dictonary with the number of occurence of each pair


def part2(path):
    file = open(path)
    data = file.read().splitlines()
    textInput = data[0]
    rules = {}
    nbIteration = 40
    for i in range(2, len(data)):
        parents, enfant = data[i].split(' -> ')
        rules[parents] = enfant
    comptagePaires = {}
    comptageChar = {}
    # le premier passage sert à initialiser les comptages des paires
    for k in range(nbIteration+1):
        nouveauComptagePaires = {}
        if k == 0:
            for i in range(len(textInput)-1):
                if textInput[i] in comptageChar.keys():
                    comptageChar[textInput[i]] += 1
                else:
                    comptageChar[textInput[i]] = 1
                if textInput[i:i+2] in rules.keys():
                    if textInput[i:i+2] in nouveauComptagePaires.keys():
                        nouveauComptagePaires[textInput[i:i+2]] += 1
                    else:
                        nouveauComptagePaires[textInput[i:i+2]] = 1
            comptagePaires = nouveauComptagePaires
            if textInput[len(textInput)-1] in comptageChar.keys():
                comptageChar[textInput[len(textInput)-1]] += 1
            else:
                comptageChar[textInput[len(textInput)-1]] = 1
        else:
            for paire, nombre in comptagePaires.items():
                elementAInserer = rules[paire]
                if paire[0]+elementAInserer in nouveauComptagePaires.keys():
                    nouveauComptagePaires[paire[0]+elementAInserer] += nombre
                else:
                    nouveauComptagePaires[paire[0]+elementAInserer] = nombre
                if elementAInserer+paire[1] in nouveauComptagePaires.keys():
                    nouveauComptagePaires[elementAInserer+paire[1]] += nombre
                else:
                    nouveauComptagePaires[elementAInserer+paire[1]] = nombre
                if elementAInserer in comptageChar.keys():
                    comptageChar[elementAInserer] += nombre
                else:
                    comptageChar[elementAInserer] = nombre
        comptagePaires = nouveauComptagePaires

    return(max(comptageChar.values())-min(comptageChar.values()))


print(part2("day14.txt"))
