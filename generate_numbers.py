"""
Рекурсия
Генерация всех перестановок

Источник: youtube.com Тимофей Кирьянов "Алгоритмы на Python 3" Лекция № 8
"""


def generate_numbers(N: int, M: int, prefix=None):
    """
    Рекурсивная генерация перестановок (с лидирующими нулями)
    в N-ричной системе счисления длины M
    :N:основание системы счисления (N<=10)
    :M: количество чисел
    :prefix: перестановки
    :return:
    """
    # фича Python! при prefix=None=False, [] = False оператор ниже
    # должен вернуть False!
    # но возвращает []
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return

    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M - 1, prefix)
        prefix.pop()  # удаление добавленного digit?


# модифицированный вариант
def find(number, A):
    """ Поиск числа number в списке A возврат True, если найден иначе False"""
    for x in A:
        if x == number:
            return True
    return False


def generate_permutations(N: int, M: int = -1, prefix=None):
    """
    Модифицированная рекурсивная генерация перестановок N чисел M длины
    в список prefix
    """

    M = N if M == -1 else M
    prefix = prefix or []
    if M == 0:
        print(*prefix, sep=',')  # развертывание списка
        return
    for number in range(1, N + 1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(N, M - 1, prefix)
        prefix.pop()

print(generate_numbers.__doc__)
generate_numbers(3,3)

print(generate_permutations.__doc__)
generate_permutations(5)
