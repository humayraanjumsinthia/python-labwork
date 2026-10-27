students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]],
    [206, "Rafi", [80, 80, 80]],
    [207, "Karim", [75, 105, 70]],
    [208, "Mina", []],
]


def calculate_average(marks):
    if marks == []:
        return 0
    total = 0
    for mark in marks:
        total = total + mark
    return total / len(marks)


def classify_performance(average):
    if average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"


def display_report(students):
    for student in students:
        student_id = student[0]
        name = student[1]
        marks = student[2]

        if marks == []:
            print(student_id, name, "No marks")
        else:
            valid = True
            for mark in marks:
                if mark < 0 or mark > 100:
                    valid = False

            if valid == False:
                print(student_id, name, "Invalid marks")
            else:
                average = calculate_average(marks)
                category = classify_performance(average)
                print(student_id, name, average, category)


display_report(students)
