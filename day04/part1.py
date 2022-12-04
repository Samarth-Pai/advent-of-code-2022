with open("input.txt") as f:
    lines = f.readlines()
    score =0
    for line in lines:
        line = line.replace("\n","").split(",")
        firstRange,secondRange = line[0],line[1]
        firstSet = set(range(int(firstRange.split("-")[0]),int(firstRange.split("-")[1])+1))
        secondSet = set(range(int(secondRange.split("-")[0]),int(secondRange.split("-")[1])+1))
        if firstSet.issubset(secondSet):
            score+=1
        elif secondSet.issubset(firstSet):
            score+=1
        else:pass
    print(score)
