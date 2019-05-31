"""
Пример работы с переменными окружения
ф-ция setenv() и переменная environ
"""
import os

key = 'USERNAME' #'USER'
print('setenv...', end=' ')
print(os.environ[key])

os.environ[key] = 'Brain' # неявный вызов ф-ции os.putenv
os.system('python echoenv.py')

os.environ[key] = 'Arthur'  # изменение передается порождаемым программам
os.system('python echoenv.py') # и связанным с процессом библ. модулям на C

os.environ[key] = input('?')
print(os.popen('python echoenv.py').read())

