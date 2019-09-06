"""
Рекурсия.
Построение фрактального прямоугольника с поворотом
Параметры: A,B,C,D кортежи координат (x,y)
        deep глубина рекурсии
Источник: youtube.com Тимофей Кирьянов "Алгоритмы на Python 3" Лекция № 7
Автор использует графич.библиотеку консольного рисования graphics
"""
import graphics as gr

# import tkinter as gr

window = gr.GraphWin('Russian game', 600, 600)
"""
alpha - доля координаты новой точки (см.видео)
"""
alpha = 0.2


def fractal_rectangle(A, B, C, D, deep=10):
    if deep < 1:
        return
    # "*A" - развернутый кортеж аналог (A[0],A[1])!!!
    # gr.Line(gr.Point(*A), gr.Point(*B)).draw(window)
    # gr.Line(gr.Point(*B), gr.Point(*C)).draw(window)
    # gr.Line(gr.Point(*C), gr.Point(*D)).draw(window)
    # gr.Line(gr.Point(*D), gr.Point(*A)).draw(window)
    # аналогично (синтаксический сахар:
    for Start, End in (A, B), (B, C), (C, D), (D, A):
        gr.Line(gr.Point(*Start), gr.Point(*End)).draw(window)

    # Вычисление координат следующих точек:
    A1 = (A[0] * (1 - alpha) + B[0] * alpha, A[1] * (1 - alpha) + B[1] * alpha)
    B1 = (B[0] * (1 - alpha) + C[0] * alpha, B[1] * (1 - alpha) + C[1] * alpha)
    C1 = (C[0] * (1 - alpha) + D[0] * alpha, C[1] * (1 - alpha) + D[1] * alpha)
    D1 = (D[0] * (1 - alpha) + A[0] * alpha, D[1] * (1 - alpha) + A[1] * alpha)
    fractal_rectangle(A1,B1,C1,D1, deep-1)  #рекурсия

if __name__ == '__main__':

    fractal_rectangle((100,100),(500,100), (500,500),(100,500))
    # input()