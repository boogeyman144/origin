def update_grades(grades):
    updated_grades = []
    for grade in grades:
        if grade == 2:
            continue
        elif grade == 3:
            updated_grades.append(4)
        else:
            updated_grades.append(grade)
    return updated_grades
grades1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
grades2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
grades3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]
updated_grades1 = update_grades(grades1)
updated_grades2 = update_grades(grades2)
updated_grades3 = update_grades(grades3)
print("Обновленные оценки 1:", updated_grades1)
print("Обновленные оценки 2:", updated_grades2)
print("Обновленные оценки 3:", updated_grades3)
