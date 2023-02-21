# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.

# Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

nunber_of_ticket = int(
    input("Введите номер билета для проверки на счастливость: "))

number_1 = int(nunber_of_ticket/100000)
print(number_1)
number_2 = int((nunber_of_ticket/10000) % 10)
print(number_2)
number_3 = int((nunber_of_ticket/1000) % 10)
print(number_3)
number_4 = int((nunber_of_ticket/100) % 10)
print(number_4)
number_5 = int((nunber_of_ticket/10) % 10)
print(number_5)
number_6 = int(nunber_of_ticket % 10)
print(number_6)

if number_1+number_2+number_3 == number_4+number_5+number_6:
    print(f'Yes! Поздравляю, это счастливый билет!')
else:
    print(f'No')
