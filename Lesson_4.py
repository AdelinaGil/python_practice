# Задание 1.
# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

def calc():
    hours = float(input('Введите количество отработанных часов : '))
    price = float(input('Введите ставку сотрудника в 1 час : '))
    bonus = float(input('Введите размер премии - '))
    pay = hours * price
    return pay + bonus
print(f'Размер заработной платы составил: {calc() }')


# Задание 2.
# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')


# Задание 3.
# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.

print(f'Числа от 20 до 240 кратные 20 или 21 - {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')


# Задание 4.
# Представлен список чисел. Определите элементы списка, не имеющие повторений.
# Сформируйте итоговый массив чисел, соответствующих требованию.
# Элементы выведите в порядке их следования в исходном списке. Для выполнения задания обязательно используйте генератор.

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_new_list = [el for el in my_list if my_list.count(el) == 1]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')


# Задание 5.
# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.

from functools import reduce

def my_func(el_p, el):
    return el_p * el

print(f'Список четных чисел {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Произведение всех элементов списка {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')


# Задание 6.
# Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее

from itertools import cycle, count

el_start = int(input('Введите число: '))
el_stop = el_start * 2 + 10 + 1

# итератор, генерирующий целые числа, начиная с указанного
for el in count(el_start):
    if el < el_stop:
        print(el)
    else:
        break
del el

# итератор, повторяющий элементы некоторого списка
my_list = [el for el in range(el_stop)]
count = 0
for i in cycle(my_list):
    if count < el_stop + 10:
        print(i)
        count += 1
    else:
        break


# Задание 7.
# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция вызывается следующим образом: for el in fact(n).
# Она отвечает за получение факториала числа. В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.

from itertools import count
from math import factorial

def fact():
    for el in count(1):
        yield factorial(el)

n = fact()
x = 0
for i in n:
    if x < 15:
        print(i)
        x += 1
    else:
        break
