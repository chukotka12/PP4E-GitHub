"""
Каркас скрипта перевода чисел в заданную систему счисления
Предполагается - исходное числов в десятичной системе.
Предполагается - исходное числов в десятичной системе.
Источник: youtube.com Тимофей Кирьянов "Алгоритмы на Python 3" Лекция № 3
"""
base = 7  # основание системы счисления
x = int(input('Введите число:'))
while x > 0:
    digit = x % base  # получение последней цифры
    print(digit, end='')
    x //= base  # зачеркнуть последнюю цифру
