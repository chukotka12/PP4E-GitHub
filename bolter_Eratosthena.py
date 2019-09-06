"""
Упрощенный вариант
Алгоритм "Решето Эратосфена"
 нахождения простых чисел до заданного натурального числа
 путем постепенного отсеивания составных чисел
Источник: youtube.com Тимофей Кирьянов "Алгоритмы на Python 3" Лекция № 5
"""

def bolterEratosphena(N):
    A = [True] * N
    A[0] = A[1] = False
    for k in range(2, N):
        if A[k]:
            for m in range(2 * k, N, k):
                A[m] = False
    for k in range(N):
        print(k, '-', 'простое' if A[k] else 'составное')


if __name__ == '__main__':
    bolterEratosphena(23)