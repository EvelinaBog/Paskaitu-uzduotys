students = {'Evelina': 10,
            'Diana': 8,
            'Tomas': 6,
            'Mindaugas': 9,
            'Brigita': 7,
            'Monika': 8,
            'Rokas': 6,
            'Matas': 9,
            'Domantas': 7,
            'Antanas': 2}

# Calculating the average grade
average = sum(students.values()) / len(students)
print(f'Students average grade: {average}')

# Creating a set of students with grades below 8
bad_students = {student for student, grade in students.items() if grade < 8}

# Checking if a specific student exists and printing the result
check = input('Check student name: ').capitalize()  # Capitalizing input for consistency
if check in bad_students:
    print(f'{check} is not among good students, grade: {students.get(check)}')
else:
    print(f"{check} is among good students, grade: {students.get(check)}.")
