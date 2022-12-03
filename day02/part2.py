# Rock paper scissor
with open("input.txt") as f:
    score = 0
    combinations = {"A X":3+0,"A Y":1+3,"A Z":2+6,
                    "B X":1+0,"B Y":2+3,"B Z":3+6,
                    "C X":2+0,"C Y":3+3,"C Z":1+6}
    lines = f.readlines()
    for line in lines:
        line = line.strip("\n")
        score+=combinations[line]
    print(score)