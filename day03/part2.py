import string
with open("input.txt") as f:
    lines = f.readlines()
    firstGroup = lines[::3]
    secondGroup = lines[1::3]
    thirdGroup = lines[2::3]
    alphaPrior = []
    for en,line in enumerate(firstGroup):
        for alpha in line.strip():
            if alpha in secondGroup[en] and alpha in thirdGroup[en]:
                alphaPrior.append(alpha)
                break
    combinations = dict(zip(string.ascii_letters,range(1,53)))
    priorityNumbers = list(map(lambda x:combinations[x],alphaPrior))
    print(sum(priorityNumbers))