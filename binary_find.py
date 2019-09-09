"""
Бинарный поиск.
Бинарный поиск О(log2N) в отсортированном массиве.
Требование: предварительно рабочий массив д.б. отсортирован.
В данном случае отсортирован по возрастанию. Левой границей принимается индекс
предыдущего (левого) элемента меньшего искомого; правой границей принимается
индекс следующего за искомым элемента.
Источник: youtube.com Тимофей Кирьянов "Алгоритмы на Python 3" Лекция № 10
"""


def left_bound(A, key):
    """ Поиск левой границы искомого диапазона"""
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] < key:
            left = middle
        else:
            right = middle
    return left


def right_bound(A, key):
    """ Поиск правой границы искомого диапазона"""
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] <= key:
            left = middle
        else:
            right = middle
    return right
