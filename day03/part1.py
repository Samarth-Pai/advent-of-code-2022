import string
with open("input.txt") as f:
    lines = f.readlines()
    alphabetPriorities = []
    for line in lines:
        halfStringLength = int(len(line) / 2)
        firstHalfLine = line[:halfStringLength]
        secondHalfLine = line[halfStringLength:]
        for alphabet in firstHalfLine:
            if alphabet in secondHalfLine:
                alphabetPriorities.append(alphabet)
                break
    combinations = dict(zip(string.ascii_letters,range(1,53)))
    priorityNumbers = list(map(lambda x:combinations[x],alphabetPriorities))
    print(sum(priorityNumbers))
