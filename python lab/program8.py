
def calculate_scores(*args, **kwargs):
    grades = list(args)

    if not grades:
        return 0, 0, 0, {}

    minimum = min(grades)
    maximum = max(grades)
    average = sum(grades) / len(grades)

    distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    for grade in grades:
        if grade >= 90:
            distribution["A"] += 1
        elif grade >= 80:
            distribution["B"] += 1
        elif grade >= 70:
            distribution["C"] += 1
        elif grade >= 60:
            distribution["D"] += 1
        else:
            distribution["F"] += 1

    print("Assessment Details:", kwargs)

    return minimum, maximum, average, distribution


grades = tuple(map(int, input("Enter grades separated by spaces: ").split()))

minimum, maximum, average, distribution = calculate_scores(
    *grades, subject="Python", class_name="BCA"
)

print("Minimum Grade:", minimum)
print("Maximum Grade:", maximum)
print("Average Grade:", round(average, 2))
print("Letter Grade Distribution:", distribution)
