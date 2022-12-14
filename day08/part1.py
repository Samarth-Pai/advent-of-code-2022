with open("input.txt") as f:
    lines = f.read().splitlines()
visibles = 0
treeArray = []
for tree in lines:
    treeRow = []
    for eachTree in tree:
        treeRow.append(int(eachTree))
    treeArray.append(treeRow)
for i in range(1, len(treeArray) - 1):
    for j in range(1, len(treeRow) - 1):
        checkingNum = treeArray[i][j]
        up, left, down, right = 1, 1, 1, 1
        for k in range(0, i):
            if treeArray[k][j] >= checkingNum:
                up = 0
        for l in range(0, j):
            if treeArray[i][l] >= checkingNum:
                left = 0
        for m in range(i + 1, len(treeArray)):
            if treeArray[m][j] >= checkingNum:
                down = 0
        for n in range(j + 1, len(treeRow)):
            if treeArray[i][n] >= checkingNum:
                right = 0
        visibles += up or left or down or right
print(visibles + 2 * (len(treeArray) + (len(treeRow) - 2)))
