with open("input.txt") as f:
    lines = f.readlines()
summ = 0
tree = {"": []}
pos = ""
for line in lines:
    line = line[:-1]
    if line[:4] == "dir ":
        try:
            tree[pos + "/" + line.split(" ")[-1]]
        except:
            tree[pos + "/" + line.split(" ")[-1]] = []
    elif line[:4] == "$ cd":
        lsMode = 0
        if line.split(" ")[-1] == "..":
            pos = pos.replace("/" + pos.split("/")[-1], "")
        elif line.split(" ")[-1] == "/":
            pos = ""
        else:
            pos += "/" + line.split(" ")[-1]
    elif line[0].isdigit():
        try:
            tree[pos].append(line.split(" ")[0])
        except:
            tree[pos] = []
            tree[pos].append(line.split(" ")[0])
    else:
        pass
dirSizes = {}
for key, value in tree.items():
    if key not in dirSizes.keys():
        dirSizes[key] = 0
    for ke in tree.keys():
        if key in ke:
            dirSizes[key] += sum(map(int, tree[ke]))

for score in dirSizes.values():
    if score <= 100000:
        summ += score
print(summ)
