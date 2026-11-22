students = {
    "Angela": 90,
    "Maria": 85,
    "John": 78,
    "David": 95,
    "Sofia": 88
}

total = 0

print("Student Name     Grade")
print("----------------------")

for name, grade in students.items():
    print(f"{name:<17}{grade}")
    total += grade

average = total / len(students)

print("----------------------")
print(f"Class Average: {average:.2f}")
