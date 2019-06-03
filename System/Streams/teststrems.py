"""
Чтение числа до символа EOF и возведение их в квадрат
Пример:
    python teststrems.py    - ввод с консоли
    python teststrems.py < input.txt    - ввод из файла
    python teststreams.py < input.txt > output.txt - ввод из файла
                                        и вывод в файл
    python teststrems.py < input.txt | more   - ввод из файла
                                        и передача другой программе

"""
def interact():
    print('Hello stream world') # выдвод в sys.stdout
    while True:
        try:
            reply = input('Enter a number >')  # чтение из sys.stdin
        except EOFError:
            break
        else:
            num = int(reply)
            print('%d square is %d' % (num, num**2))
    print('Bye')


if __name__ == '__main__':
    interact()