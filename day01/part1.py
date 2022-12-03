with open("input.txt") as f:
    lines = f.readlines()
    calories = 0
    caloriesList = []
    for line in lines:
        if line == "\n":
            caloriesList.append(calories)
            calories = 0
        else:
            calories+=int(line)
    print(max(caloriesList))