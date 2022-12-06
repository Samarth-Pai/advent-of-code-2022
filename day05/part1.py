with open("input.txt") as f:
    lines  = f.readlines()
score = 0
iIndx = 0
fullStack = {}
fIndx = 4
stack = {}
stoppedIndex = 0
for en,line in enumerate(lines):
    if line[0:4].strip()=="1":
        stoppedIndex = en
        break
    stack[en+1]=[]
    for i in range(len(line)//4):
        stack[en+1] = stack[en+1]+[line[iIndx:fIndx].replace("\n","").strip()]
        iIndx+=4
        fIndx+=4
    iIndx = 0
    fIndx = 4
for i in range(len(list(stack.values())[0])):
    fullStack[i+1]=[]
    for eachStack in stack.values():
        if eachStack[i]!="":
            fullStack[i+1]=fullStack[i+1]+[eachStack[i]]
    fullStack[i+1] = list(reversed(fullStack[i+1]))
for line in lines[stoppedIndex+2:]:
    line = line.replace("move","").replace("\n","")
    splittedLine = line.split("from")
    howMuch = int(splittedLine[0])
    from_ = int(splittedLine[1].split("to")[0])
    to = int(splittedLine[1].split("to")[1])
    for times in range(howMuch):
        fullStack[to].append(fullStack[from_][-1])
        fullStack[from_].pop(-1)
for values in fullStack.values():
    print(values[-1][1],end="")