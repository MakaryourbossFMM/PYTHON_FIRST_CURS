# ДЗ 1, задача 5 «Сданные экзамены» (★★★)
# Задачник, задача 2.1.13: https://python-theory-makarov.vercel.app/zadachnik/2-1/index.html#p13
#
# Студент сдал три экзамена. Экзамен сдан, если балл не меньше 40. Вводятся три балла. Выведите,
# сколько экзаменов сдано и сданы ли все три.
#
# Каждый input() выводит подсказку. Тексты подсказок — как в примерах, после двоеточия или скобки
# стоит пробел.
#
# Пример 1
#   ввод:
#     55
#     40
#     90
#   в терминале:
#     Балл за первый экзамен: 55
#     Балл за второй экзамен: 40
#     Балл за третий экзамен: 90
#     Сдано экзаменов: 3
#     Сессия закрыта: True
# Пример 2
#   ввод:
#     39
#     70
#     12
#   в терминале:
#     Балл за первый экзамен: 39
#     Балл за второй экзамен: 70
#     Балл за третий экзамен: 12
#     Сдано экзаменов: 1
#     Сессия закрыта: False

# Решение
first_exam = int(input("Балл за первый экзамен: "))
second_exam = int(input("Балл за второй экзамен: "))
third_exam = int(input("Балл за третий экзамен: "))

first_exam_passed = False
second_exam_passed = False
third_exam_passed = False

if first_exam >= 40:
    first_exam_passed = True

if second_exam >= 40:
    second_exam_passed = True
 
if third_exam >= 40:
    third_exam_passed = True

print("Сдано экзаменов: ", first_exam_passed + second_exam_passed + third_exam_passed)
if first_exam_passed and second_exam_passed and third_exam_passed:
    print("Сессия закрыта: True")
else:
    print("Сессия закрыта: False")