god = int(input('Какой год вы хотите проверить: '))
if ((god % 4 == 0) and (god % 4 != 0)) or (god % 4 == 0):
    print('Год високосный')
else:
    print('Год не високосный')