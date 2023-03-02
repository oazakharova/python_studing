# Задаем длину списка, наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль, сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

import random

length = int(input(f'Введите длину списка: '))
random_list = [random.randint(3, 10) for _ in range(length)]
print(random_list)

number = int(input(f'Введите число для поиска в списке: '))

if number in random_list:
    dict = {}
    for item in random_list:
        dict[item] = dict.get(item, 0) + 1
    # print(dict)
    print(
        f'Данное число встречается в списке следующее количество раз - {dict[number]}')

else:
    set = set(random_list)
    print(set)
    sorted_random_list = sorted(set)
    min_element = sorted_random_list[0]
    max_element = sorted_random_list[-1]
    print(sorted_random_list)
    print(f'Минимальный элемент - {min_element}')
    print(f'Максимальный элемент - {max_element}')

    list_1_part = [n for n in sorted_random_list if n < number]
    print(list_1_part)
    pretender_1 = list_1_part[-1]
    print(pretender_1)
    difference_1 = abs(number-pretender_1)
    print(difference_1)

    list_2_part = [n for n in sorted_random_list if n > number]
    print(list_2_part)
    pretender_2 = list_2_part[0]
    print(pretender_2)
    difference_2 = abs(number-pretender_2)
    print(difference_2)

    if number > min_element and number < max_element:
        if difference_1 < difference_2:
            print(
                f'Введенного числа нет в сформированном списке, ближайшее к нему - {pretender_1}')
        else:
            print(
                f'Введенного числа нет в сформированном списке, ближайшее к нему - {pretender_2}')

    else:  # вот это все не работает
        if number < min_element:
            print(
                f'Введенного числа нет в сформированном списке, ближайшее к нему - {min_element}')

        else:
            print(
                f'Введенного числа нет в сформированном списке, ближайшее к нему - {max_element}')

    # if number < min_element:
    #     print(
    #         f'Введенного числа нет в сформированном списке, ближайшее к нему - {min_element}')

    # if number > max_element:
    #     print(
    #         f'Введенного числа нет в сформированном списке, ближайшее к нему - {max_element}')

    # if difference_1 < difference_2:
    #     print(
    #         f'Введенного числа нет в сформированном списке, ближайшее к нему - {pretender_1}')
    # if difference_1 > difference_2:
    #     print(
    #         f'Введенного числа нет в сформированном списке, ближайшее к нему - {pretender_2}')
