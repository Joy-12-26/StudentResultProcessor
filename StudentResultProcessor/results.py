def calculate_total(marks):
    total = 0
    for m in marks:
        total += m
    return total


def calculate_average(total, num_subjects):
    return total / num_subjects


def calculate_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"
