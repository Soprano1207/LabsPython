groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    }
]


def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15),
              student["surname"].ljust(10),
              str(student["exams"]).ljust(30),
              str(student["marks"]).ljust(20))
        
print("\nСписок студентов:")
print_students(groupmates)


def filter_by_average(students, min_avg):
    filtered = []
    for student in students:
        avg = sum(student["marks"]) / len(student["marks"])
        #по условию avg должен быть выше (значит >). Если выше или равен (изменить на >=) 
        if avg > min_avg: 
            filtered.append(student)
    return filtered


user_input = float(input("\nВведите минимальный средний балл для фильтрации: "))
result = filter_by_average(groupmates, user_input)

print("\nСтуденты со средним баллом выше", user_input)
print_students(result)