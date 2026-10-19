#простая конструкция
temperature = 28   

if temperature > 25: # условие можно в скобках писать если удобно
        print("Сегодня жарко")

print("Проверка завершенна") 



#Конструкция и else
age = 17

if age >= 18:
    print("Доступ разрешён")
else:
    print("Доступ закрыт")





#Конструкция с if elif else
grade = 100
if grade >= 90:
    print("Отлично")
elif grade >= 80:
    print("Хорошо")
elif grade >= 70:
    print("Удовлетворительно")
else:
    print("Нужно повторить тему")




#Два независимых if
number = 10

if number > 0:
    print("Положительное число")

if number > 5:
    print("Число больше пяти")