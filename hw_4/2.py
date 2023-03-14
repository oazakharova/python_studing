# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения


def print_operation_table(operation, num_rows, num_columns):
    result = 0
    for i in range(1, num_rows+1):
        for j in range(1, num_columns+1):
            print("%4d" % (i * j), end="")  # красивый вывод без смещения
        print()


def operation(x, y):
    return (x*y)


num_rows = int(input(f'Введите число строк: '))
num_columns = int(input(f'Введите число столбцов: '))
print_operation_table(operation, num_rows, num_columns)
