def get_Average(marks):
    total_sum = sum(marks)
    total_sum = float(total_sum)
    return total_sum / len(marks)


def calculate_total_Average(student):
    assignment = get_Average(student["assignment"])
    test = get_Average(student["test"])
    lab = get_Average(student["lab"])

    return 0.1 * assignment + 0.7 * test + 0.2 * lab


def assign_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'E'


def class_Average_is(student_list):
    result_list = []

    for student in student_list:
        stud_avg = calculate_total_Average(student)
        result_list.append(stud_avg)
    return get_Average(result_list)


if __name__ == '__main__':
    # 1. Jack's dictionary
    jack = {
        "name": "Jack Frost",
        "assignment": [80, 50, 40, 20],
        "test": [75, 75],
        "lab": [78.20, 77.20]
    }

    # 2. James's dictionary
    james = {
        "name": "James Potter",
        "assignment": [82, 56, 44, 30],
        "test": [80, 80],
        "lab": [67.90, 78.72]
    }

    # 3. Dylan's dictionary
    dylan = {
        "name": "Dylan Rhodes",
        "assignment": [77, 82, 23, 39],
        "test": [78, 77],
        "lab": [80, 80]
    }

    # 4. Jessica's dictionary
    jess = {
        "name": "Jessica Stone",
        "assignment": [67, 55, 77, 21],
        "test": [40, 50],
        "lab": [69, 44.56]
    }

    # 5. Tom's dictionary
    tom = {
        "name": "Tom Hanks",
        "assignment": [29, 89, 60, 56],
        "test": [65, 56],
        "lab": [50, 40.6]
    }

    students = [jack, james, dylan, jess, tom]

    for student in students:
        avg = calculate_total_Average(student)
        print("Average marks of %s is: %s" % (student["name"], avg))
        print("Letter grade of %s is: %s" %
              (student["name"], assign_letter_grade(avg)))
        print()

    class_avg = class_Average_is(students)
    print("Class average is %s" % (class_avg))
    print("Letter grade of the class is: %s" % assign_letter_grade(class_avg))
