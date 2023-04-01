# Считываем данные из входного файла "Выполнение.txt"
with open("Выполнение.txt", "r") as f:
    data = {}
    for line in f:
        parts = line.strip().split()
        surname, group, lab_number, lab_theme, date, mark = parts
        key = int(lab_number)
        if key not in data:
            data[key] = []
        data[key].append({"surname": surname, "group": group, "date": date, "mark": int(mark)})

    # Подсчитываем количество студентов и средний балл для каждой лабораторной работы
    results = []
    for lab_number, students in data.items():
        num_students = len(students)
        avg_mark = sum([s["mark"] for s in students]) / num_students
        results.append({"lab_number": lab_number, "lab_theme": students[0]["lab_theme"], "num_students": num_students, "avg_mark": avg_mark})

    # Сортируем список лабораторных работ по убыванию среднего балла
    results.sort(key=lambda x: x["avg_mark"], reverse=True)

    # Записываем результаты в выходной файл "Сложность.txt"
    with open("Сложность.txt", "w") as f:
        f.write("Номер_пп Номер_лабы Тема_Лабы Число_выполнивших Средний_балл\n")
        for i, r in enumerate(results, start=1):
            f.write(f"{i} {r['lab_number']} {r['lab_theme']} {r['num_students']} {r['avg_mark']:.2f}\n")

    # Подсчитываем количество выполненных лабораторных работ и средний балл для каждого студента
    students_data = {}
    for students in data.values():
        for student in students:
            surname = student["surname"]
            lab_number = student["lab_number"]
            mark = student["mark"]
            if surname not in students_data:
                students_data[surname] = {"num_labs": 0, "total_mark": 0}
            students_data[surname]["num_labs"] += 1
            students_data[surname]["total_mark"] += mark

    # Вычисляем средний балл для каждого студента
    for student_data in students_data.values():
        student_data["avg_mark"] = student_data["total_mark"] / student_data["num_labs"]

    # Сортируем список студентов по убыванию среднего балла
    students_results = [{"surname": k, "num_labs": v["num_labs"], "avg_mark": v["avg_mark"]} for k, v in students_data.items()]
    students_results.sort(key=lambda x: x["avg_mark"], reverse=True)

    # Записываем результаты в выходной файл "Рейтинг.txt"
    with open("Рейтинг.txt", "w") as f:
        f.write("Номер_пп Фамилия Число_Лаб Средний_балл\n")
        for i, r in enumerate(students_results, start=1):
            f.write(f"{i} {r['surname']} {r['num_labs']} {r['





