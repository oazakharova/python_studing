# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# 3, 5 - 243

def exponentiation_number_to_degree(number, degree):
    if degree == 1:
        return number
    if degree == 0:
        number = 1
        return number
    if degree > 1:
        return number*exponentiation_number_to_degree(number, degree-1)
    if degree < 0:
        return 1/(number*exponentiation_number_to_degree(number, -degree-1))


number = int(input(f'Введите число: '))
degree = int(input(f'Введите степень: '))
print(exponentiation_number_to_degree(number, degree))
