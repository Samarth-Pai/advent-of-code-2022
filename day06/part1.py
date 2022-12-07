with open("input.txt") as f:
    line = f.read()
score = 0
print(line)
from_ = 0
to = 4
marker = str()
while True:
    for alpha in line[from_:to]:
        if line[from_:to].count(alpha) > 1:
            from_ += 1
            to += 1
    if marker == line[from_:to]:
        print(to)
        exit()
    marker = line[from_:to]
