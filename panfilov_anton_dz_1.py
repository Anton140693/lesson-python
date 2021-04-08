# Задание №1

# Вариант a)
duration = int(input('Введите количество секунд: '))
s = str(duration)
print(s + ' сек ')

# Вариант b)
duration = int(input('Введите количество секунд: '))
m = str((duration //60) % 60)
s = str(duration % 60)
print(m + ' мин ' + s + ' сек ')


# Вариант c)
duration = int(input('Введите количество секунд: '))
h = str(duration // 3600)
m = str((duration //60) % 60)
s = str(duration % 60)
print(h + ' час ' + m + ' мин ' + s + ' сек ')


# Вариант d*)
duration = int(input('Введите количество секунд: '))
d = str(duration // 86400)
h = str((duration // 3600) % 24)
m = str((duration //60) % 60)
s = str(duration % 60)
print(d + ' дн ' + h  + ' час ' + m + ' мин ' + s + ' сек ')


# Задание №2

my_list = []
for num in range(1, 1001, 2):
    my_list.append(num ** 3)
# a
final_sum = 0  # финальный ответ
for num in my_list:
    check_sum = 0  # сумма всех цифр конкретного числа
    for check_num in str(num):
        check_sum += int(check_num)
    if check_sum % 7 == 0:
        final_sum += num
print(final_sum)

# b&c
final_sum = 0
for num in my_list:
    num += 17  # отличие от a
    check_sum = 0
    for check_num in str(num):
        check_sum += int(check_num)
    if check_sum % 7 == 0:
        final_sum += num
print(final_sum)


#  Задание №3
percent = int(input('Введите число процента: '))
if percent == 1:
    word = 'процент'
elif percent <= 4:
    word = 'процента'
else:
    word = 'процентов'
print(percent, word)
