students = {
    "Angela": [90, 85, 95],
    "Maria": [80, 90, 85],
    "John": [75, 80, 85],
    "David": [95, 90, 100],
    "Sofia": [85, 88, 92]
}

def calculate_averages(students):
    averages = []

    for name, grades in students.items():
        average = sum(grades) / len(grades)
        averages.append([name, average])

    return averages


print("Student Name     Average")
print("------------------------")

averages = calculate_averages(students)

for student in averages:
    print(f"{student[0]:<17}{student[1]:.2f}")

print("------------------------")

grade1 = sum(grades[0] for grades in students.values()) / len(students)
grade2 = sum(grades[1] for grades in students.values()) / len(students)
grade3 = sum(grades[2] for grades in students.values()) / len(students)

print(f"Class Average Grade 1: {grade1:.2f}")
print(f"Class Average Grade 2: {grade2:.2f}")
print(f"Class Average Grade 3: {grade3:.2f}")
