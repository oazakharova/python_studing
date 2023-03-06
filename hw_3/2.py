# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

def get_sum(number1, number2):
    if number2 == 1:
        return number1+number2
    else:
        return get_sum(number1+1, number2-1)


number1 = int(input(f'Введите число 1: '))
number2 = int(input(f'Введите число 2: '))
print(get_sum(number1, number2))
