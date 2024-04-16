
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
average = sum(students.values()) / len(students)
print(f'Students average grade: {average}')

bad_students = set()
for key, value in students.items():
    if value < 8:
        bad_students.add(key)
while True:
    check = input('Check student name: ')
    if check.capitalize() in bad_students:
        print(f'{check.capitalize()} is not among good students, grade: {students.get(check.capitalize())}')
    elif check.capitalize() in students:
        print(f"{check.capitalize()} is among good students, grade: {students.get(check.capitalize())}.")
        break
    else:
        print('There is no such student in the list')
