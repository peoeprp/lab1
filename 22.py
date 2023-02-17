mesto = int(input('Введите номер вашего места: '))
if mesto in range(37,54):
    if mesto % 2 == 0:
        print('У вас боковое верхнее место')
    else:
        print('У вас боковое нижнее место')
if mesto in range(1,36):
    if mesto % 2 == 0:
        print('У вас верхнее место')
    else:
        print('У вас нижнее место')