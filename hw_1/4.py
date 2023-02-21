# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

length_of_chocolate = int(input(f'Введите длину шоколадки: '))
width_of_chokolate = int(input(f'Введите ширину шоколадки: '))
quantity = int(input(f'Введите желаемое количество долек: '))

if (float(quantity % length_of_chocolate) == 0) or (float(quantity % width_of_chokolate) == 0):
    print(f'Yes')
else:
    print(f'No')
