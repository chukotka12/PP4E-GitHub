"""
Сценарий для отображения значения переменной окружения
вызываемый и setenv.py
"""
import os

key = 'USERNAME' #'USER'
print('echoenv...', end=' ')
print('Hello, ', os.environ[key])
