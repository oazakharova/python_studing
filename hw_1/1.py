# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = int(input("Введите трехзначное число для нахождения суммы его цифр: "))

number_1 = int(n/100)
number_2 = int((n / 10) % 10)
number_3 = int(n % 10)

sum_of_numbers = number_1 + number_2 + number_3
print(f'Сумма цифр введенного числа = {sum_of_numbers}')
