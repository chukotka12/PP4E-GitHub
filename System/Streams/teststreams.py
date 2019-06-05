"""
Пример перенаправления входного и выходного потоков
Чтение чисел до символа конца файла и возведение их в квадрат
Пример: python teststreams.py < input.txt > output.txt
        перенаправление входного потока данных из файла input.txt
        перенаправление выходного потока во файл output.txt
        или передача выхода на вход другой программы (конвейер)
        python teststreams.py < input.txt | more
"""


def interact():
    print('Hello stream world')  # вывод в sys.stdout
    while True:
        try:
            reply = input('Enter a number>')  # чтение из sys.stdin
        except EOFError:
            break
        else:
            num = int(reply)
            print('%d squared is %d' % (num, num ** 2))
    print('Bye')

if __name__ == '__main__':
    interact()
