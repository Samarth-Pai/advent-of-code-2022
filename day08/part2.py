with open("input.txt") as f:
    lines = f.read().splitlines()
scScore = []
treeArray = []
for tree in lines:
    treeRow = []
    for eachTree in tree:
        treeRow.append(int(eachTree))
    treeArray.append(treeRow)

for i in range(1, len(treeArray) - 1):
    for j in range(1, len(treeRow) - 1):
        checkingNum = treeArray[i][j]
        views = 0
        upView, leftView, downView, rightView = 0, 0, 0, 0
        up, left, down, right = 1, 1, 1, 1
        for k in range(i - 1, -1, -1):

            if treeArray[k][j] >= checkingNum:
                upView += 1
                up = 0
                break
            if up and (treeArray[k][j] < checkingNum):
                upView += 1

        for l in range(j - 1, -1, -1):
            if treeArray[i][l] >= checkingNum:
                leftView += 1
                left = 0
                break
            if left and treeArray[i][l] < checkingNum:
                leftView += 1

        for m in range(i + 1, len(treeArray)):
            if treeArray[m][j] >= checkingNum:
                downView += 1
                down = 0
                break
            if down and treeArray[m][j] < checkingNum:
                downView += 1

        for n in range(j + 1, len(treeRow)):
            if treeArray[i][n] >= checkingNum:
                rightView += 1
                right = 0
                break
            if right and treeArray[i][n] < checkingNum:
                rightView += 1

        views = upView * leftView * downView * rightView
        scScore.append(views)
print(max(scScore))