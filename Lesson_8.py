# Задание 1.
# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return f'Данные соотвествуют действительности'
                else:
                    return f'Неверные данные года. Такой год еще не наступил'
            else:
                return f'Неверные данные месяца'
        else:
            return f'Неверные данные дня'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('07 - 04 - 2022')
print(today)
print(Data.valid(111, 12, 2025))
print(today.valid(12, 13, 2010))
print(Data.extract('12 - 12 - 2012'))
print(today.extract('20 - 02 - 2002'))
print(Data.valid(2, 12, 2021))


# Задание 2.
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class DivisionByNull:
    def __init__(self, dividend, divisor):
        self.divider = dividend
        self.denominator = divisor

    @staticmethod
    def divide_by_null(dividend, divisor):
        try:
            return (dividend / divisor)
        except:
            return (f"Деление на 0 невозможно")

div = DivisionByNull(2000, 10)
print(DivisionByNull.divide_by_null(10, 0))
print(DivisionByNull.divide_by_null(1, 0.25))
print(div.divide_by_null(10000, 20))


# Задание 3.
# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка.

class Exception:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите значение и нажмите Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение")
                y_or_n = input(f'Попробовать еще раз? Yes/Stop ')

                if y_or_n == 'yes' or y_or_n == 'Yes':
                    print(try_except.my_input())
                elif y_or_n == 'Stop' or y_or_n == 'stop':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'

try_except = Exception(1)
print(try_except.my_input())


# Задание 4.
# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

# Задание 5.
# Продолжить работу над первым заданием.
# Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).

# Задание 6.
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class OfficeEquipment:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'


    def reception(self):
        try:
            unit = input(f'Введите наименование устройства')
            unit_p = int(input(f'Введите цену за единицу '))
            unit_q = int(input(f'Введите количество '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Сейчас на складе -\n {self.my_store_full}')
            return f'Выход'
        else:
            return OfficeEquipment.reception(self)


class Printer(OfficeEquipment):
    def to_print(self):
        return f'для печати {self.numb}'


class Scanner(OfficeEquipment):
    def to_scan(self):
        return f'для сканирования {self.numb}'


class Copier(OfficeEquipment):
    def to_copier(self):
        return f'для копирования  {self.numb} '


unit_1 = Printer('Epson', 60000, 15, 1)
unit_2 = Copier('Canon', 120000, 1, 5)
unit_3 = Scanner('Xerox', 15000, 2, 10)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_2.to_copier())


# Задание 7.
# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, n, m, *args):
        self.a = n
        self.b = m
        self.z = 'n + m * i'

    def __add__(self, other):
        print(f'Сумма I1 и I2 равна')
        return f'I = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение I1 и I2 равно')
        return f'I = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'I = {self.a} + {self.b} * i'


I_1 = ComplexNumber(-1, 2)
I_2 = ComplexNumber(30, 2)
print(I_1)
print(I_1 + I_2)
print(I_1 * I_2)


