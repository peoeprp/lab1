password = input('Введите пароль: ')
is_numeric = False
is_upper = False
is_lower = False
is_spec = False
for char in password:
    if char.isnumeric():
        is_numeric = True
    elif char.islower():
        is_lower = True
    elif char.isupper():
        is_upper = True
    elif char in "@#%&":
        is_spec = True
if len(password) > 6 and is_numeric and is_lower and is_upper and is_spec:
    print('Надежный пароль!')
else:
    if len(password) < 6:
        print ('Пароль слишком короткий')
    if is_numeric == False:
        print('Пароль должен содержать цифры')
    if is_lower == False:
        print('Пароль должен содержать строчные буквы')
    if is_spec == False:
        print('Пароль должен содержать заглавные буквы')
    if is_spec == False:
        print('Пароль должен содержать специальные символы')