# Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."

first = int(input('Введите Ваш возраст: '))
second = int(input('Введите Ваш id: '))
third = int(input('Введите случайное число: '))

if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)



