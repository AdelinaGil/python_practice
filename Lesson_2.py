# Задание 1.
# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

List_Of_deiails = [365, None, -7890, 'Hello!', False, 3.14, -5.5]
def my_type(el):
    for el in range(len(List_Of_deiails)):
        print(type(List_Of_deiails[el]))
    return
my_type(List_Of_deiails)
print("Задание 1 выполнено")


# Задание 2.
# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

elements_count = int(input("Введите количество элементов - "))
list_of_data = []
n = 0
m = 0
while n < elements_count:
    list_of_data.append(input("Введите следующее значение списка - "))
    n += 1

for elem in range(int(len(list_of_data)/2)):
        list_of_data[m], list_of_data[m + 1] = list_of_data[m + 1], list_of_data[m]
        m += 2
print(list_of_data)
print("Задание 2 выполнено")


# Задание 3.
# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
month = int(input("Введите номер месяца от 1 до 12: "))
if month ==1 or month == 12 or month == 2:
        print(seasons_dict.get(1))
        print(seasons_list[0])
elif month == 3 or month == 4 or month ==5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])
elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
        print("Такого месяца не существует")
print("Задание 3 выполнено")


# Задание 4.
# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

user_str = input("Введите фразу ")
user_word = []
num = 1
for el in range(user_str.count(' ') + 1):
    user_word = user_str.split()
    if len(str(user_word)) <= 10:
        print(f" {num} {user_word [el]}")
        num += 1
    else:
        print(f" {num} {user_word [el] [0:10]}")
        num += 1
print("Задание 4 выполнено")


# Задание 5.
# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
print ("Для остановки введите отрицательное число")
user_number = int(input("Введите натуральное число - "))
while user_number > -1:
    for el in range(len(my_list)):
        if my_list[el] == user_number:
            my_list.insert(el + 1, user_number)
            break
        elif my_list[0] < user_number:
            my_list.insert(0, user_number)
        elif my_list[-1] > user_number:
            my_list.append(user_number)
        elif my_list[el] > user_number and my_list[el + 1] < user_number:
            my_list.insert(el + 1, user_number)
    print(f"текущий рейтинг - {my_list}")
    user_number = int(input("Введите число "))
else: print(f"Ввод завершен. Финальный рейтинг - {my_list}")
print("Задание 5 выполнено")

# Задание 6*.
# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами,
# то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.

# Нужно собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например, название.
# Тогда значение — список значений-характеристик, например, список названий товаров.

goods = []
specifications = {'наименование': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analytics = {'наименование': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0
specifications_ = None
manage = None
while True:
    manage = input("Для остановки введите 'Q', для продолжения 'Enter', для вывода аналитики нажмите 'A'").upper()
    if manage == 'Q':
        break
    num += 1
    if manage == 'A':
        print(f'\n Текущая аналитика - \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in specifications.keys():
        specifications_ = input(f'Введите данные "{f}"')
        specifications[f] = int(specifications_) if (f == 'цена' or f == 'количество') else specifications_
        analytics[f].append(specifications[f])
    goods.append((num, specifications))
print("Задание 6 выполнено")
