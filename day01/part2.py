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
    top3calorieSum = 0
    for i in range(3):
        top3calorieSum+=max(caloriesList)
        caloriesList.remove(max(caloriesList))
    print(top3calorieSum)