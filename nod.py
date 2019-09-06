"""
Рекурсия
Алгоритм Евклида (наибольший общий делитель) Grand Common Diviser
НОД(a,b) = НОД(a-b,b)

Источник: youtube.com Тимофей Кирьянов "Алгоритмы на Python 3" Лекция № 7
"""


def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    else:  # a < b
        return gcd(a, b - a)


# оптимизация: НОД(b, a % b)
def gcd_opt(a, b):
    if b == 0:
        return a
    else:
        return gcd_opt(b, a % b)


# оптимизация 2 (сахар)
def gcd_opt2(a, b):
    return a if b == 0 else gcd_opt2(b, a % b)
